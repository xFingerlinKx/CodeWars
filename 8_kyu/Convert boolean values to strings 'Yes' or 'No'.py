"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""


def bool_to_word_1(boolean):
    return 'Yes' if boolean else 'No'


def bool_to_word_2(boolean):
    return ['No', 'Yes'][boolean]
