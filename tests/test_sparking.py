'''
@author: allen
'''
import pytest
from sparking.sparking import Sparking

class TestSparking(object):
    @pytest.mark.parametrize("bits_num, key, expected", [
        (8, 5, 6),
        (64, 5, 62)
    ])
    def testcase(self, bits_num, key, expected):

        assert Sparking.testcase(bits_num, key) == expected


# class TestSparking(object):
#     @pytest.mark.parametrize("bits_num, key, expected", [
#         (8, 5, 6),
#         (64, 5, 62)
#     ])
#     def testcase(self, bits_num, key, expected):
#         assert Sparking.testcase(bits_num, key) == expected




















