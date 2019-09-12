"""
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'.
If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'.
If there are no good ideas, as is often the case, return 'Fail!'.
"""


def well_1(x):
    if x.count('good') in range(1, 3):
        return 'Publish!'
    elif x.count('good') > 2:
        return 'I smell a series!'
    elif x.count('good') == False:
        return 'Fail!'


def well_2(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'
