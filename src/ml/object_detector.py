from ultralytics import YOLO
import logging

logger = logging.getLogger(__name__)

class SpecializedDetector:
    def __init__(self, model_path="models/yolo/citizenship.pt"):
        logger.info(f"Loading YOLO model: {model_path}")
        self.model = YOLO(model_path)

    def detect(self, image):
        """Runs detection and returns JSON data + visual image."""
        results = self.model.predict(image, conf=0.4, verbose=False)
        result = results[0]  # Get first result
        
        detections = []
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = self.model.names[int(box.cls[0])]
            conf = float(box.conf[0])
            detections.append({
                "label": label,
                "confidence": round(conf, 2),
                "bbox": [x1, y1, x2, y2]
            })
            
        # This is the image with boxes/labels drawn on it
        visual_img = result.plot() 
        
        return detections, visual_img