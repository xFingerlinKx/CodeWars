"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.
"""


def maps_1(a):
    return [num * 2 for num in a]


def maps_2(a):
    return map(lambda x: 2 * x, a)
