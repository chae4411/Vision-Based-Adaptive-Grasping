import cv2
from vision.camera import Camera
from vision.detector import ObjectDetector

def main() -> None:
    camera = Camera()
    detector = ObjectDetector()
    
    try:
        while True:
            frame = camera.read()
            results = detector.detect(frame)
            annotated_frame = results[0].plot()
            cv2.imshow("Adaptive Grasp Vision", annotated_frame,)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()