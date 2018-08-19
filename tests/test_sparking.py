'''
@author: allen
'''
import pytest
from sparking.sparking import Sparking

class TestSparking(object):
    @pytest.mark.parametrize("bits_num, key, expected", [
        (0, 0, 1),
        (0, 0, 2),
        (0, 0, 3),
        (0, 0, 4)
    ])
    def test_get_num_of_one(self, bits_num, key, expected):
        assert Sparking.get_num_of_one(bits_num, key) == expected

    @pytest.mark.parametrize("bits_num, key, expected", [
        (8, 5, 6),
        (32, 5, 30),
        (64, 5, 62)
    ])
    def testcase(self, bits_num, key, expected):
        assert Sparking.testcase(bits_num, key) == expected




















