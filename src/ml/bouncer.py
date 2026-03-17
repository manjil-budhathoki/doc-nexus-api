from ultralytics import YOLO
import os

class DocumentBouncer:
    """
        We will use the yolo model of the document-detection
        to load the model and detect the document type.
    """
    def __init__(self):
        self.model_path = "models/yolo/best.pt"
        self.model = YOLO(self.model_path)

        self.class_names = self.model.names

    def get_document_type(self,image):
        """
        Returns the name of the document citizenship or demat
        """
        results = self.model.predict(image,conf=0.5, verbose=False)


        detected_labels = []
        for r in results:
            for box in r.boxes:
                label = self.model.names[int(box.cls[0])]
                detected_labels.append(label)
        

        if any("demat" in l.lower() for l in detected_labels):
            return "demat"
        
        elif any("citizenshipid" in l.lower() for l in detected_labels):
            return "citizenship"
        
        return None
    