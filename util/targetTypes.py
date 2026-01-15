from targetSpec import TargetSpec
import numpy as np

TARGET_SPECS = [
    TargetSpec(
        name="Vegas 1 Spot",
        numTargets=1,
        numCircles=11,
        scoreVector=np.array([10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    ),
    TargetSpec(
        name="NFAA 5 Spot",
        numTargets=5,
        numCircles=4,
        scoreVector=np.array([5, 5, 4, 4, 0])
    ),
    TargetSpec(
        name="Vegas 3 Spot",
        numTargets=3,
        numCircles=4,
        scoreVector=np.array([0, 10, 9, 8, 7])
    ),
    TargetSpec(
        name="NFAA 1 Spot",
        numTargets=1,
        numCircles=6,
        scoreVector=np.array([5, 5, 4, 3, 2, 1, 0])
    )
]
