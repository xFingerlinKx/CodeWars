"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""


def positive_sum_1(arr):
    sum = 0

    for num in arr:
        if num >= 0:
            sum += num
        else:
            None
    return sum


def positive_sum_2(arr):
    return sum(x for x in arr if x > 0)
