"""
Simple, remove the spaces from the string, then return the resultant string.
"""


def no_space_1(x):
    l = []
    for elem in x.split(' '):
        if elem != '':
            l.append(elem)

    return ''.join(l)


def no_space_2(x):
    return x.replace(' ', '')


def no_space_3(x):
    s = ''.join(x.split())
    return s
