"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F

"""


def abbrevName_1(name):
    name = name.split(' ')
    return ('{}.{}'.format(name[0][0], name[1][0])).upper()


def abbrevName_2(name):
    return '.'.join(w[0] for w in name.split()).upper()


def abbrevName_3(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]
