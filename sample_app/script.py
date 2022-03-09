import numpy as np


def non_zero(array: np.ndarray) -> bool:
    if np.any(array):
        return True
    else:
        return False
