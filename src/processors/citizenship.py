import logging
import cv2
from .base import DocumentProcessor
from src.ml.object_detector import SpecializedDetector
from src.ml.ocr_reader import OCRReader
from src.utils.text_processor import process_robust_text

logger = logging.getLogger(__name__)

class CitizenshipProcessor(DocumentProcessor):
    def __init__(self):
        self.detector = SpecializedDetector(model_path="models/yolo/citizenship.pt")
        self.ocr = OCRReader()

    def extract_and_verify(self, image, detections, user_input):
        # 1. Get Landmarks
        landmarks, _ = self.detector.detect(image)
        labels = [d['label'] for d in landmarks]
        
        # 2. Face Detection
        face = "front" if "photo_region" in labels else "back"
        script = "nepali" if face == "front" else "english"

        # 3. Find Primary Text Block (Your old logic)
        text_regions = [d for d in landmarks if d["label"] == "text_block_primary"]
        
        raw_text = ""
        if text_regions:
            # Taking the first primary block found
            x1, y1, x2, y2 = text_regions[0]["bbox"]
            raw_crop = image[y1:y2, x1:x2]
            
            # THE MAGIC: Your old white padding logic!
            processed_crop = cv2.copyMakeBorder(
                raw_crop, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 255]
            )
            
            # Read Text
            raw_text = self.ocr.read_text(processed_crop, script=script)
        else:
            # Fallback
            raw_text = self.ocr.read_text(image, script=script)

        # Normalize using your old robust logic
        normalized_text = process_robust_text(raw_text)

        return {
            "face": face,
            "raw_text": raw_text,
            "normalized_text": normalized_text
        }

    def validate(self, extracted_data, user_input):
        from src.utils.matching_engine import verify_name, verify_id_number, verify_dob
        
        raw = extracted_data['raw_text']
        norm = extracted_data['normalized_text']
        
        return {
            "name": verify_name(user_input.get('name', ''), raw, norm),
            "id_number": verify_id_number(user_input.get('id_number', ''), raw, norm),
            "dob": verify_dob(user_input.get('dob', ''), raw, norm)
        }