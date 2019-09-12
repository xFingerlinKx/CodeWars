"""
Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array.
"""


def is_vow_1(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]


def is_vow_2(inp):
    for i, v in enumerate(inp):
        if chr(v) in 'aeiou':
            inp[i] = chr(v)
    return inp

