from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class TargetSpec:
    name: str
    numTargets: int
    numCircles: int
    scoreVector: np.ndarray
