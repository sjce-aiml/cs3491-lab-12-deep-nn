"""Public tests for Lab 12. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab12 as lab  # noqa: E402

import numpy as np

def test_relu():
    assert np.allclose(lab.relu(np.array([-1.0, 2.0])), [0, 2])
