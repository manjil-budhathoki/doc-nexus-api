import cv2
import numpy as np
import logging
from paddleocr import PaddleOCR

logger = logging.getLogger(__name__)

class OCRReader:
    def __init__(self):
        logger.info("Initializing PROVEN Old OCR Engines...")
        # Exact settings from your old engines.py
        self.ne_ocr = PaddleOCR(lang='ne', enable_mkldnn=False, rec_batch_num=1, show_log=False)
        self.en_ocr = PaddleOCR(lang='en', enable_mkldnn=False, rec_batch_num=1, show_log=False)

    def ensure_rgb(self, image):
        """Your old ensure_rgb function"""
        if len(image.shape) == 2:
            return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        elif image.shape[2] == 4:
            return cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        return image

    def parse_paddle_result(self, results):
        """Your exact old robust parser"""
        text_list = []
        if not results: return ""
        if isinstance(results, list):
             for res in results:
                if hasattr(res, 'keys') and 'rec_texts' in res:
                    text_list.extend(res['rec_texts'])
                    continue
                if hasattr(res, 'rec_texts') and res.rec_texts:
                    text_list.extend(res.rec_texts)
                    continue
                if isinstance(res, list):
                    for line in res:
                        if len(line) == 2 and isinstance(line[1], tuple):
                             text_list.append(line[1][0])
                        elif isinstance(line, tuple) and len(line) == 2:
                            text_list.append(line[0])
        return " ".join(text_list).strip()

    def read_text(self, raw_crop, script="nepali"):
        if raw_crop is None or raw_crop.size == 0:
             return ""

        crop = self.ensure_rgb(raw_crop)
        crop = np.ascontiguousarray(crop)
        
        engine = self.en_ocr if script == "english" else self.ne_ocr

        try:
            paddle_results = engine.ocr(crop)
            text = self.parse_paddle_result(paddle_results)
            return text
        except Exception as e:
            logger.error(f"Paddle Error: {e}")
            return ""