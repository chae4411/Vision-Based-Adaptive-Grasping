import cv2

class Camera: 
    def __init__(self, camera_index: int = 0) -> None:
        self.capture = cv2.VideoCapture(camera_index)
        
        if not self.capture.isOpened():
            raise RuntimeError("Unable to open camera.")
        
    def read(self):
        success, frame = self.capture.read()
        
        if not success:
            raise RuntimeError("Unable to read camera frame.")
        
        return frame
    
    def release(self) -> None:
        self.capture.release()
        