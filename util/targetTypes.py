from targetSpec import TargetSpec
import numpy as np

TARGET_SPECS = [
    TargetSpec(
        name="Vegas 1 Spot",
        numTargets=1,
        numCircles=10,
        scoreVector=np.array([10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
        centers=np.array([[500, 500]]),
        radii=np.array([
            24.04192257, 46.48654175, 90.91151810, 136.85043526, 182.78935242, 226.81414032, 271.24053955, 316.99087524, 361.04649353, 406.98182678, 451.97720337
        ])
    ),
    TargetSpec(
        name="NFAA 5 Spot",
        numTargets=5,
        numCircles=4,
        scoreVector=np.array([5, 5, 4, 4, 0]),
        centers=[(784, 228), (506, 508), (226, 228), (224, 790), (782, 786)],
        radii=np.array([48.36448441, 94.82338867, 140.44796295, 186.91786957])
    ),
    TargetSpec(
        name="Vegas 3 Spot",
        numTargets=3,
        numCircles=6,
        scoreVector=np.array([0, 10, 9, 8, 7]),
        centers=[(500, 338), (280, 720), (716, 718)],
        radii=np.array([20.84759108, 40.34269842, 77.1244278, 118.93515523, 159.32479095, 198.60931905])
    ),
    TargetSpec(
        name="NFAA 1 Spot",
        numTargets=1,
        numCircles=6,
        scoreVector=np.array([5, 5, 4, 3, 2, 1, 0]),
        centers=np.array([(500,500)]),
        radii=np.array([46.369422912597656, 93.85966873168945, 185.36888885498047, 277.6470184326172, 370.0227813720703, 462.2470703125])

    )
]
