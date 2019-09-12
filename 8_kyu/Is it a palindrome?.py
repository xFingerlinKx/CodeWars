"""
Write function isPalindrome that checks if a given string (case insensitive) is a palindrome.

In Racket, the function is called palindrome?

(palindrome? "nope") ; returns #f
(palindrome? "Yay")  ; returns #t
"""


def is_palindrome_1(s):
    return s.lower() == s[::-1].lower()


def is_palindrome_2(s):
    s = s.lower()
    return s == s[::-1]
