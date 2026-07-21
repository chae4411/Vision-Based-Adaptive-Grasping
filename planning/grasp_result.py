from dataclasses import dataclass
from planning.grasp_types import GraspType

@dataclass
class GraspResult:
    grasp_type: GraspType
    center: tuple[int, int]
    point1: tuple[int, int]
    point2: tuple[int, int]
    angle: float
    score: float