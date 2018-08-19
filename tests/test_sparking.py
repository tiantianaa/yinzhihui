'''
@author: allen
'''
import pytest
from sparking.sparking import Sparking

class TestSparking(object):
    # @pytest.mark.parametrize("bits_num, key, expected", [
    #     (0, 0, 1),
    #     (0, 0, 2),
    #     (0, 0, 3),
    #     (0, 0, 4)
    # ])
    # def test_get_num_of_one(self, bits_num, key, expected):
    #     assert Sparking.get_num_of_one(bits_num, key) == expected


    @pytest.mark.parametrize("bits_num, key, expected", [
        (8, 5, 2),
        (16, 5, 2),
        (32, 5, 2),
        (64, 5, 2)
    ])

    def testpoint(self, bits_num, key, expected):
        assert Sparking.testpoint(bits_num, key) == expected



















