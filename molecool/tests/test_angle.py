"""
Unit and regression test for the measure module.
"""

# Import package, test suite, and other packages as needed
import molecool
import numpy as np

def test_calculate_angle():
    """Test that calculate_distance function calculates what we expect."""
    
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])
    
    expected_angle = 90

    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_angle == calculated_angle

