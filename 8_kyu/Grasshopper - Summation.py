"""
Summation

Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3 1 + 2

summation(8) -> 36 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

(summation 2) ; 3  (+ 1 2)
(summation 8) ; 36 (+ 1 2 3 4 5 6 7 8)
"""


def summation_1(num):
    summa = 0
    for x in range(1, num + 1):
        summa += x

    return summa


def summation_2(num):
    return sum(range(1, num + 1))
