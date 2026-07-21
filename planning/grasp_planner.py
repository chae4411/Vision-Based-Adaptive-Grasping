import math
import numpy as np

from planning.grasp_result import GraspResult
from planning.grasp_types import GraspType
from vision.object_analyzer import ObjectFeature

class GraspPlanner:
    def plan(self, obj: ObjectFeature) -> GraspResult:
        grasp_type, score = self._select_grasp_type(obj)
        grasp_angle = self._normalize_angle(obj.orientation)
        
        point1 = self._find_boundary_point(
            mask = obj.mask,
            center = obj.centroid,
            angle_degrees = grasp_angle,
        )
        
        point2 = self._find_boundary_point(
            mask = obj.mask,
            center = obj.centroid,
            angle_degrees = grasp_angle + 180.0,
        )
        
        return GraspResult(
            grasp_type = grasp_type,
            center = obj.centroid,
            point1 = point1,
            point2 = point2,
            angle = grasp_angle,
            score = score,
        )
    
    def _select_grasp_type(
        self,
        obj: ObjectFeature,
    ) -> tuple[GraspType, float]:
        aspect_ratio = obj.aspect_ratio
        
        if aspect_ratio < 1.3:
            return GraspType.SPHERICAL, 0.90
        
        if aspect_ratio >= 4.0:
            return GraspType.PINCH, 0.85
        
        if aspect_ratio >= 1.8:
            return GraspType.POWER, 0.80
        
        return GraspType.LATERAL, 0.70
    
    def _find_boundary_point(
        self,
        mask: np.ndarray,
        center: tuple[int, int],
        angle_degrees: float,
    ) -> tuple[int, int]:
        height, width = mask.shape[:2]
        
        center_x, center_y = center
        angle_radians = math.radians(angle_degrees)
        
        direction_x = math.cos(angle_radians)
        direction_y = math.sin(angle_radians)
        
        previous_point = center
        max_distance = int(math.hypot(width, height))
        
        for distance in range(1, max_distance):
            current_x = int(round(center_x + direction_x * distance))
            current_y = int(round(center_y + direction_y * distance))
            
            if (current_x < 0 or current_x >= width or current_y < 0 or current_y >= height):
                break
            if mask[current_y, current_x] == 0:
                break
            
            previous_point = (current_x, current_y)
        return previous_point
    
    @staticmethod
    def _normalize_angle(angle: float) -> float:
        while angle >= 180.0:
            angle -= 180.0
        
        while angle < 0.0:
            angle += 180.0
        
        return angle
            
        