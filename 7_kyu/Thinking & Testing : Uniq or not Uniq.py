"""
Only by Thinking and Testing

def testit(a, b):
    a.extend(b) # extend???
    return a

TEST CASIES:

test.assert_equals(testit([0],[1]), [0,1], "")
test.assert_equals(testit([1,2],[3,4]), [1,2,3,4], "")
test.assert_equals(testit([1],[2,3,4]), [1,2,3,4], "")
test.assert_equals(testit([1,2,3],[4]), [1,2,3,4], "")
test.assert_equals(testit([1,2],[1,2]), [1,1,2,2], "")

"""


def testit(a, b):
    return sorted(list(set(a)) + list(set(b)))
