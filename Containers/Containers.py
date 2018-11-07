"""
Homework 07

Practice using lists, tuples, dictionaries, and sets.
"""

import unittest
from collections import defaultdict
from collections import Counter

"""
Part 1:
Write a function to check if two strings are anagrams (if the characters in 
the first word can be rearranged to make the second word, then they are anagrams)

1. Using only strings and lists
2. Using defaultdict
3. Using Counters
"""
def anagrams(str1, str2):
    """ using lists to implement anagrams checking """
    """ NOTE: using sorted() to return sorted list, using .sort() would return None """
    return sorted(list(str1)) == sorted(list(str2)) # sorting as lists have order

def anagrams_dd(str1, str2):
    """ using defaultdict to implement anagrams checking """
    freq = defaultdict(int)

    for c in str1:  # count the occurrences in str1
        freq[c] += 1

    for s in str2:  # count the occurrences in str2 by subtracting 1 for each occurrence
        freq[s] -= 1

    return not any(freq.values())  # if all occurrences in str2 is 0, then return true

def anagrams_cc(str1, str2):
    """ using Counters to implement anagrams checking """
    return sorted(Counter(str1).most_common(len(str1))) == sorted(Counter(str2).most_common(len(str2)))
    # sorting as dictionary has no order in case two chars have the same occurrences.

class AnagramsTest(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(anagrams('cinema', 'iceman'))
        self.assertTrue(anagrams('', ''))
        self.assertTrue(anagrams('dormitory', 'dirtyroom'))
        self.assertFalse(anagrams('cinemaaa', 'iceman'))
        self.assertFalse(anagrams('Python', 'python'))

    def test_anagrams_dd(self):
        self.assertTrue(anagrams_dd('cinema', 'iceman'))
        self.assertTrue(anagrams_dd('', ''))
        self.assertTrue(anagrams_dd('dormitory', 'dirtyroom'))
        self.assertFalse(anagrams_dd('cinemaaa', 'iceman'))
        self.assertFalse(anagrams_dd('Python', 'python'))

    def test_anagrams_cc(self):
        self.assertTrue(anagrams_cc('cinema', 'iceman'))
        self.assertTrue(anagrams_cc('', ''))
        self.assertTrue(anagrams_cc('dormitory', 'dirtyroom'))
        self.assertFalse(anagrams_cc('cinemaaa', 'iceman'))
        self.assertFalse(anagrams_cc('Python', 'python'))

"""
Part 2:
Write a function covers_alphabet(sentence) that returns True if sentence 
includes at least one instance of every character in the alphabet or False 
using only Python sets.

NOTE: the sentence may also include other symbols.
"""
def covers_alphabet(sentence):
    chars = set()
    for c in sentence.lower():
        chars.add(c)

    return chars >= set('abcdefghijklomnopqrstuvwxyz')

class CoverAlphabetTest(unittest.TestCase):
    def test_covers_alphabet(self):
        self.assertTrue(covers_alphabet("abcdefghijklomnopqrstuvwxyz"))
        self.assertTrue(covers_alphabet("aabbcdefghijklomnopqrstuvwxyzzabc"))
        self.assertTrue(covers_alphabet("The quick brown fox jumps over the lazy dog"))
        self.assertTrue(covers_alphabet("We promptly judged antique ivory buckles for the next prize"))
        self.assertTrue(covers_alphabet("We promptly ++judged antique ivory &&buckles for the next prize"))
        self.assertFalse(covers_alphabet(" "))
        self.assertFalse(covers_alphabet("I love Python"))

"""
Part 3: Book Index
Write a function of book index listing all of the words in the book along with 
a unique list of pages where that word occurs anywhere in the book.

The input is a list of where each item in the list is a tuple with a word and 
the page where the word appears.

Return a list where each word appears once in alphabetical order along with a 
sorted list of distinct pages where the word occurs.  
The items in the result should be sorted by words and the pages should be sorted 
in ascending order.
"""
def book_index(words):
    dic = defaultdict(set)

    for word in words:
        dic[word[0]].add(word[1])

    index = [ [item, sorted(list(dic[item]))] for item in dic]

    return sorted(index)

class BookIndexTest(unittest.TestCase):
    def test_book_index(self):
        woodchucks = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1),
                      ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2),
                      ('could', 2), ('chuck', 1), ('wood', 1)]

        self.assertTrue(book_index(woodchucks) == [['a', [1]], ['chuck', [1, 3]], ['could', [2]],
                                                   ['how', [3]], ['if', [1]], ['much', [3]],
                                                   ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)