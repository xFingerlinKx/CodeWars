"""
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
"""


def check_1(seq, elem):
    return True if elem in seq else False


def check_2(seq, elem):
    return elem in seq
