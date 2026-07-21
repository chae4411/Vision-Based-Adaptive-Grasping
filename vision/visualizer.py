import cv2
import numpy as np

from planning.grasp_result import GraspResult

class GraspVisualizer:
    def draw(
        self, 
        frame: np.ndarray,
        result: GraspResult,
    ) -> np.ndarray:
        output = frame.copy()
        
        cv2.line(
            output,
            result.point1,
            result.point2,
            (255, 255, 255),
            2,
        )
        
        cv2.circle(
            output,
            result.point1,
            6,
            (0, 0, 255),
            -1,
        )
        
        cv2.circle(
            output,
            result.point2,
            6,
            (0, 0, 255),
            -1,
        )
        
        cv2.circle(
            output,
            result.center,
            5,
            (0, 255, 0),
            -1,
        )
        
        text_x = max(10, result.center[0] - 100)
        text_y = max(30, result.center[1] - 40)
        
        strategy_text = (
            f"Grasp: {result.grasp_type.value.upper()}"
            f"({result.score:.2f})"
        )
        
        angle_text = f"Angle: {result.angle:.1f} deg"
        
        cv2.putText(
            output,
            strategy_text,
            (text_x, text_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0), 
            2,
        )
        
        cv2.putText(
            output,
            angle_text,
            (text_x, text_y + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (0, 255, 0),
            2,
        )
        
        return output