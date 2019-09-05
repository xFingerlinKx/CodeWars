"""
Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have
the right tails. To help her, you must correct the broken function to make sure that the second argument (tail),
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be strings, and normal letters.
"""


def correct_tail_1(body, tail):
    return True if body[-1] == tail else False


def correct_tail_2(body, tail):
    return body[-1] == tail


def correct_tail_3(body, tail):
    return body.endswith(tail)
