import cv2

from planning.grasp_planner import GraspPlanner
from vision.camera import Camera
from vision.detector import ObjectDetector
from vision.object_analyzer import ObjectAnalyzer
from vision.visualizer import GraspVisualizer

def main() -> None:
    camera = Camera()
    detector = ObjectDetector()
    analyzer = ObjectAnalyzer()
    planner = GraspPlanner()
    visualizer = GraspVisualizer()
    
    try:
        while True:
            frame = camera.read()
            results = detector.detect(frame)
            result = results[0]
            annotated_frame = result.plot()
            
            if result.masks is not None and result.boxes is not None:
                for index, mask_data in enumerate(result.masks.data):
                    mask = mask_data.cpu().numpy()
                    
                    frame_height, frame_width = frame.shape[:2]
                    resized_mask = cv2.resize(
                        mask,
                        (frame_width, frame_height),
                        interpolation = cv2.INTER_NEAREST,
                    )
                    
                    class_id = int(result.boxes.cls[index].item())
                    label = result.names[class_id]
                    confidence = float(result.boxes.conf[index].item())
                    
                    ignored_labels = {"person"}
                    if label in ignored_labels:
                        continue
                    if confidence < 0.60:
                        continue
                    
                    try:
                        object_feature = analyzer.analyze(
                            mask = resized_mask,
                            label = label,
                            confidence = confidence,
                        )
                        if object_feature.area < 2000:
                            continue
                        
                        grasp_result = planner.plan(object_feature)
                        annotated_frame = visualizer.draw(
                            frame = annotated_frame,
                            result = grasp_result,
                        )
                    except ValueError as error:
                        print(f"Object analysis skipped: {error}")
                    
            cv2.imshow("Vision-Based Adaptive Grasping", annotated_frame,)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()