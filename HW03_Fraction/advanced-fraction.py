"""
Homework 02 -- Fraction

Implement a fraction calculator including operations:
1. ask the user for two fractions and an operator;
2. a class implementing fraction calculating;
3. a test case to demonstrate that the calculator works correctly;
4. print the results.

"""


class Fraction:
    """
    Implement addition, subtraction, multiplication, division and comparison of two fractions
    """
    def __init__(self, numerator, denominator):
        """
        set the numerator and denominator of a fraction
        raise a ValueError Exception when the denominator is zero
        """
        self.num = numerator
        self.den = denominator


        if self.den == 0:
            raise ZeroDivisionError("Error! The denominator of a fraction cannot be zero!")

    def plus(self, other):
        """
        return a fraction with the addition of self and other
        """
        newnum = self.num * other.den + other.num * self.den
        newden = self.den * other.den
        return Fraction(newnum, newden)
        # return Fraction(newnum, newden)

    def minus(self, other):
        """
        return a fraction with the subtraction of self and other
        """
        newnum = self.num * other.den - other.num * self.den
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def times(self, other):
        """
        return a fraction with the product of self and other
        """
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def divide(self, other):
        """
        return a fraction representing the result that self divided by other
        """
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def equal(self, other):
        """
        identify whether self is equal to other, return True/False
        Hint: compare the product of the numerator of self and the denominator of other
              to the product of the numerator of other and the denominator of self.
        """
        return self.num * other.den == self.den * other.num


    def __str__(self):
        """
        return a string to display the Fraction
        """
        return "{}/{}".format(self.num , self.den)


def test_suite():
    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f128 = Fraction(12, 8)
    f32 = Fraction(3, 2)

    print("The fraction is", f12, ' [1/2] ')
    print(f12, '+', f12, '=', f12.plus(f12), '  [4/4]')
    print(f12, '+', f12, '+', f12, '=', f12.plus(f12).plus(f12), '  [12/8]')
    print(f12, '-', f44, '=', f12.minus(f44), '  [-4/8]')
    print(f12, '*', f44, '=', f12.times(f44), '  [4/8]')
    print(f12, '/', f32, '=', f12.divide(f32), '  [2/6]')
    print(f128, "==", f32, "is", f128.equal(f32), '  [True]\n')


def get_number(prompt):
    """
    read and return an integer from the user.
    cite: hw02-outline.py
    """
    while True:
        inp = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print('Error:', inp, 'is not a number. Please try again...')

def get_fraction():
    while True:
        num = get_number("Enter the numerator:")
        den = get_number("Enter the denominator:")

        try:
            f = Fraction(num, den)
            return f
        except ZeroDivisionError as e:
            print(e)

def compute(f1, operator, f2):
    if operator == '+':
        result = f1.plus(f2)
    elif operator == '-':
        result = f1.minus(f2)
    elif operator == '*':
        result = f1.times(f2)
    elif operator == '/':
        result = f1.divide(f2)
    elif operator == '==':
        result = f1.equal(f2)
    return result


def main():
    """
    Fraction Calculator
    """
    print('Welcome to the fraction calculator!')

    f1 = get_fraction()

    operator = input("\nOperation (+, -, *, /, ==):")
    while True:
        if operator in ['+', '-', '*', '/', '==']:
            break
        else:
            print("Error!", operator, "is an invalid operator! Please try again...")
            operator = input("Operation (+, -, *, /, ==):")

    f2 = get_fraction()

    result = compute(f1, operator, f2)

    print("\nThe result is\n", f1, operator, f2, "=", result)


if __name__ == '__main__':
    main()