import cv2

from vision.camera import Camera
from vision.detector import ObjectDetector
from vision.object_analyzer import ObjectAnalyzer

def main() -> None:
    camera = Camera()
    detector = ObjectDetector()
    analyzer = ObjectAnalyzer()
    
    try:
        while True:
            frame = camera.read()
            results = detector.detect(frame)
            result = results[0]
            
            if result.masks is not None:
                for index, mask_data in enumerate(result.masks.data):
                    mask = mask_data.cpu().numpy()
                    
                    class_id = int(result.boxes.cls[index].item())
                    label = result.names[class_id]
                    
                    confidence = float(result.boxes.conf[index].item())
                    
                    feature = analyzer.analyze(
                        mask = mask,
                        label = label,
                        confidence = confidence,
                    )
                    
                    print(feature)
            
            annotated_frame = results[0].plot()
            cv2.imshow("Adaptive Grasp Vision", annotated_frame,)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()