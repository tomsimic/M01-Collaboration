"""
Program: M05_Programming_Assignment-Testing.py
Author: Tomi Simic
Last date modified: 2024-04-19
This program is to be used for M05 Programming Assignment - Testing
"""
import unittest
import logging
logging.basicConfig(filename='results.log', level=logging.DEBUG)


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == '__main__':
    # logging.info(unittest.main())
    logging.debug(unittest.main())
