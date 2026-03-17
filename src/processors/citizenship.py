from .base import DocumentProcessor

class CitizenshipProcessor(DocumentProcessor):
    def extract_and_verify(self, image, detections, user_input):
        return {"type": "citizenship", "data": "dummy"}
    def validate(self, extracted_data, user_input):
        return {"status": "success"}