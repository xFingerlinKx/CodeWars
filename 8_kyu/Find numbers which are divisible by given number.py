"""
Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor.
First argument is an array of numbers and the second is the divisor.

Example:

divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
"""


def divisible_by_1(numbers, divisor):
    l = []
    for num in numbers:
        if num % divisor == 0:
            l.append(num)

    return l


def divisible_by_2(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]
