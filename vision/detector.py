from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_name: str = "yolo11n-seg.pt") -> None:
        self.model = YOLO(model_name)
    
    def detect(self, frame):
        return self.model(frame, verbose=False)