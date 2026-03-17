import pytesseract
import cv2
import re
import logging
from .base import DocumentProcessor

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DematProcessor(DocumentProcessor):
    def extract_and_verify(self, image, detections, user_input):
        logger.info("Starting Demat Extraction...")

        # 1. Image Check
        if image is None:
            logger.error("Image is empty!")
            return {"error": "Invalid image"}

        # 2. Robust Grayscale conversion
        # If image is already color (3 channels), convert to Gray
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image # Already grayscale
            
        # 3. OCR Extraction
        logger.info("Running Tesseract OCR...")
        text = pytesseract.image_to_string(gray)
        
        # 4. Parsing
        patterns = {
            "name": r"Name\s+(.*)",
            "boid": r"BOID\s+(\d+)",
            "dob": r"Date Of Birth\s+(\d{4}-\d{2}-\d{2})",
            "citizenship": r"Citizenship Number\s+(.*)",
            "contact": r"Contact Number\s+(\d+)"
        }
        
        extracted = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            extracted[key] = match.group(1).strip() if match else None
            
        logger.info(f"Extraction complete: {extracted}")
        return extracted

    def validate(self, extracted_data, user_input):
        logger.info("Validating data...")
        report = {}
        for key, value in user_input.items():
            ext_val = extracted_data.get(key)
            report[key] = {
                "match": str(ext_val).lower() == str(value).lower() if ext_val else False,
                "extracted": ext_val
            }
        return report