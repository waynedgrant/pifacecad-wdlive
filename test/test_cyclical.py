# Copyright 2015 Wayne D Grant (www.waynedgrant.com)
# Licensed under the MIT License

import unittest

from cyclical import Cyclical


class TestCyclical(unittest.TestCase):

    def test_none(self):
        try:
            Cyclical(None)
        except RuntimeError as e:
            self.assertEqual("items cannot be None", str(e))
        else:
            self.fail()

    def test_empty_list(self):
        try:
            Cyclical([])
        except RuntimeError as e:
            self.assertEqual("items must contain at least one item", str(e))
        else:
            self.fail()

    def test_one_item_list(self):
        testee = Cyclical([1])
        self.assertEqual(1, testee.current())
        testee.next()
        self.assertEqual(1, testee.current())
        testee.previous()
        self.assertEqual(1, testee.current())

    def test_two_item_list(self):
        testee = Cyclical([1, 2])
        self.assertEqual(1, testee.current())
        testee.next()
        self.assertEqual(2, testee.current())
        testee.previous()
        self.assertEqual(1, testee.current())
        testee.previous()
        self.assertEqual(2, testee.current())
        testee.next()
        self.assertEqual(1, testee.current())

if __name__ == '__main__':
    unittest.main()
