"""
Create a function that finds the integral of the expression passed.

In order to find the integral all you need to do is add one to the exponent (the second number), and divide the coefficient by that new number (the first number).

In 3x^2, for example, the integral would be 1x^3 (we added 1 to the exponent, and divided the coefficient by that new number).

integrate(3,2) // => "1x^3"
integrate(12,5) // => "2x^6"

Note that the output should be a string. The coefficient is always positive, and the result will always be an integer. Neither number will ever be 0.
"""


def integrate_1(coefficient, exponent):
    return str(coefficient // (exponent + 1)) + 'x^' + str(exponent + 1)


def integrate_2(coefficient, exponent):
    exponent += 1
    coefficient = coefficient / exponent if coefficient % exponent else coefficient // exponent
    return f"{coefficient}x^{exponent}"
