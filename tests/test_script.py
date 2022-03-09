import numpy as np

from sample_app.script import non_zero


def test_non_zero():
    array = np.ones(10)
    assert non_zero(array)

    array = np.zeros(16)
    assert not non_zero(array)

    array = np.zeros(16)
    array[4] = 5
    assert non_zero(array)
