"""
This method, which is supposed to return the result of dividing its first argument by its second,
isn't always returning correct values. Fix it.
"""


def divide_numbers_1(x, y):
    if (x / y) % 2 == 0:
        return int(x / y)
    else:
        return x / y


def divide_numbers_2(x, y):
    return float(x) / y
