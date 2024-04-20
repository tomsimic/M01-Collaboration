"""
Program: M05_Programming_Assignment-Testing.py
Author: Tomi Simic
Last date modified: 2024-04-19
This program is to be used for M05 Programming Assignment - Testing
"""


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


if __name__ == "__main__":
    test_sum()
    print("Everything passed")
