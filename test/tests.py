import unittest
from core.core import EzhenCore


class EzhenTests(unittest.TestCase):
    def test_is_me(self):
        res = EzhenCore().is_me('эжень,')
        print(res)

    def test_def_action(self):
        res = EzhenCore().def_action(['посоветуй', 'фильм'])
        print(res)

    def test_do_action(self):
        ezhen = EzhenCore()
        action = ezhen.def_action(['посоветуй', 'фильм'])
        res = ezhen.do_action(action)

        print(res)
