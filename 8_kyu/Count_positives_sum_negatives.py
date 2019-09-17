"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers
and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.
Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
"""


def count_positives_sum_negatives_1(arr):
    positive_nums_count = len([num for num in arr if num > 0])
    negative_nums_sum = sum([neg_num for neg_num in arr if neg_num < 0])
    return [] if arr == [] else [positive_nums_count, negative_nums_sum]


def count_positives_sum_negatives_2(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
