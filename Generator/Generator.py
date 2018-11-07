"""
Homework 4 -- Iterator, Generator

Author : Minghui Jin
"""

import unittest

"""
Part 1:
Write a function count_vowels(s) that takes a string as an argument and
returns the number of vowels ('a', 'e', 'i' 'o', 'u'') in the string.
"""
def count_vowels(s):  # s is a sequence
    """ return the number of vowels in the string """
    count = 0
    # Method 1:
    # for i in range(len(s)): # lower() can only work in string or character
    #     if s[i].lower() in "aeiou":
    #         count += 1

    # Method 2:
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

class Test(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)
        self.assertEqual(count_vowels(''), 0)


"""
Part 2:
Write a function that takes two arguments: (1) a target item to find,and (2) a list.
Return the index (offset from 0) of the last occurrence of the target item or None 
if the target is not found.
"""
def find_target(target, list):
    """ return the index of the last occurrence of target"""
    # Method 1: from begin to end to find the last occurrence
    # index = None
    # for i in range(len(list)):
    #     if list[i] == target:
    #         index = i
    # return index

    # Method 2: from end to begin, the first time find the target, then return
    for i in range(len(list)-1, -1, -1):
        if list[i] == target:
            return i
    return None

class FindTargetTest(unittest.TestCase):
    def test_find_target(self):
        list = [20, 1, 30, 1, 44]
        self.assertEqual(find_target(20, list), 0)
        self.assertEqual(find_target(1, list), 3)
        self.assertEqual(find_target(99, list), None)
        self.assertEqual(find_target('a', 'another'), 0)
        self.assertEqual(find_target('a', 'anaconda'), 7)
        self.assertEqual(find_target('p', 'Pycharm'), None)
        self.assertEqual(find_target('+', 'Pych+ar*m'), 4)


""" 
Part 3:
Simplify fractions by finding the Greatest Common Factor (GCF) and 
then dividing the number and denominator.
"""
class Fraction:
    """
    Implement Fraction setting
    """
    def __init__(self, numerator, denominator):
        """
        set the numerator and denominator of a fraction
        raise a ValueError Exception when the denominator is zero
        """
        self.num = numerator
        self.den = denominator

        if self.den < 0:
            self.den *= -1
            self.num *= -1

        if self.den == 0:
            raise ZeroDivisionError("Error! The denominator of a fraction cannot be zero!")

    def gcf(self):
        """ return the simplified fraction """
        newnum = abs(self.num)
        newden = abs(self.den)
        while newden > 0:
            newnum, newden = newden, newnum%newden
        com = newnum

        return Fraction(self.num/com, self.den/com)

class FractionTest(unittest.TestCase):
    def test_init(self):
        f = Fraction(1, 2)
        self.assertTrue(f)
        f2 = Fraction(1, -2)
        self.assertEqual(f2.num, -1)
        self.assertEqual(f2.den, 2)
        with self.assertRaises(ZeroDivisionError):
            f3 = Fraction(1, 0)

    def test_gcf(self):
        f1 = Fraction(9, 27)
        self.assertTrue(f1.gcf().num == 1, f1.gcf().den == 3)
        f2 = Fraction(9, -27)
        self.assertTrue(f2.gcf().num == -1, f2.gcf().den == 3)
        f3 = Fraction(8, 4)
        self.assertTrue(f3.gcf().num == 2, f3.gcf().den == 1)
        f4 = Fraction(7, 19)
        self.assertTrue(f4.gcf().num == 7, f4.gcf().den == 19)
        f5 = Fraction(-12, -16)
        self.assertTrue(f5.gcf().num == 3, f5.gcf().den == 4)


""" 
Part 4:
Write a function that provides the same functionality WITHOUT calling enumerate(). 
"""
# def my_enumerate(seq):
#     """ return a list of offset and element in the list """
#     list = []
#
#     if seq == None:
#         raise ValueError('Error!Input cannot be None!')
#
#     for i in range(len(seq)):
#         element = i, seq[i]
#         list.append(element)
#     return list

def my_enumerate(seq):
    # offset = 0
    # for item in seq:
    #     yield offset, item
    #     offset += 1
    if seq == None:
        raise ValueError('Error!Input cannot be None!')
    for offset in range(len(seq)):
        yield offset, seq[offset]


class EnumerateTest(unittest.TestCase):
    def test_my_enumerate(self):
        l = 'abc'
        self.assertTrue(list(my_enumerate(l)) == list(enumerate(l)))
        week = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
        self.assertEqual(list(my_enumerate(week)), list(enumerate(week)))
        none = None
        with self.assertRaises(ValueError):
            list(my_enumerate(none))


"""
Part 5:
Write a funtion to ask for a random number from a generator, then return the times that try to 
get the target. If the target is never found within the maximum attempts, then return None
"""
import random

def integers(min_val, max_val):
    """ generate a random number """
    while True:
        num = random.randint(min_val, max_val)
        yield num

def find(target = 3, min_val = 1, max_val = 10, attempts = 100): # default values
    """ return the times until the target is found """
    if target < min_val or target > max_val:
        raise ValueError("Error! Target cannot be smaller than the minimum or larger than the maximum!")
    elif min_val > max_val:
        raise ValueError("Error! min value cannot be larger than max value")



    # count = 1
    # for num in integers(min_val, max_val):
    #     if num == target:
    #         return count
    #     else:
    #         count += 1
    #         if count == attempts:
    #             return None

    # for cnt, val in enumerate(integers(min_val, max_val)):
    #     print('cnt = {} val = {}'.format(cnt, val))
    #     if val == target:
    #         return cnt + 1
    #     elif cnt >= attempts:
    #         break
    # return None

    g = integers(min_val, max_val)
    for cnt in range(attempts):
        # m = next(g)

        # m = next(integers(min_val, max_val))
        # This is wrong. Everytime calls a generator, it would start again
        # In this case, it is ok as the generator outputs a random number

        m = g.__next__()
        if m == target:
            return cnt + 1
    return None

class FindTest(unittest.TestCase):
    def test_find(self):
        self.assertEqual(find(3,3,3,10), 1)
        self.assertTrue(find(3, 2, 3, 10) < 10 or find(3, 2, 3, 10) == None)
        with self.assertRaises(ValueError):
            find(0, 2, 3, 10)
            find(20, 1,10, 10)
            find(0, 15, 2, 0)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
