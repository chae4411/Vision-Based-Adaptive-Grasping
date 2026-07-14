from dataclasses import dataclass

import cv2
import numpy as np

@dataclass
class ObjectFeature:
    label: str
    confidence: float
    area: float
    centroid: tuple[int, int]
    width: float
    height: float
    aspect_ratio: float
    orientation: float

class ObjectAnalyzer: 
    def analyze(
        self,
        mask: np.ndarray,
        label: str,
        confidence: float,
    ) -> ObjectFeature:
        binary_mask = (mask > 0.5).astype(np.uint8) * 255
        #print(binary_mask.shape)
        #print(binary_mask.dtype)
        #print(binary_mask.min())
        #print(binary_mask.max())
        #print(len(contours))        
        #print(area)
        
        contours, _ = cv2.findContours(
            binary_mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )
        if not contours:
            raise ValueError("No contour found in mask.")
        contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(contour)
        
        moments = cv2.moments(contour)
        if moments["m00"] == 0:
            raise ValueError("Unable to calculate centroid.")
        center_x = int(moments["m10"] / moments["m00"])
        center_y = int(moments["m01"] / moments["m00"])
        centroid = (center_x, center_y)
        
        #rotated_rect = cv2.minAreaRect(contour)
        (_, _), (width, height), orientation = cv2.minAreaRect(contour)
        short_side = min(width, height)
        long_side = max(width, height)
        if short_side == 0:
            raise ValueError("Invalid object dimensions.")
        aspect_ratio = long_side / short_side
        
        return ObjectFeature(
            label = label,
            confidence = confidence,
            area = area,
            centroid = centroid,
            width = short_side,
            height = long_side,
            aspect_ratio = aspect_ratio,
            orientation = orientation,
        )
        
