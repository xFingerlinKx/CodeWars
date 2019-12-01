"""

If　a = 1, b = 2, c = 3 ... z = 26

Then l + o + v + e = 54

and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice stronger than love :-)

The input will always be in lowercase and never be empty.

"""


def words_to_marks_1(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    summ = 0
    for letter in s:
        index = alphabet.index(letter) + 1
        summ += index
    return summ


def words_to_marks_2(s):
    return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)
