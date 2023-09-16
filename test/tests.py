import unittest
from core.core import EzhenCore


class EzhenTests(unittest.TestCase):
    def test_is_me(self):
        res = EzhenCore().is_me('эжень,')
        print(res)
