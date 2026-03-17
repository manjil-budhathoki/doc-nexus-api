from .base import DocumentProcessor

class DematProcessor(DocumentProcessor):
    def extract_and_verify(self, image, detections, user_input):
        return {"type": "demat", "data": "dummy"}
    def validate(self, extracted_data, user_input):
        return {"status": "success"}