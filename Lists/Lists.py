"""
Homework 06

List practice, Insertion Sort, Binary Tree
"""
import unittest

"""
Part 1:
Write a function remove_vowels(str) that uses a list comprehension and
returns a copy of the string with no vowels.
"""
def remove_vowels(str):
    """ return a copy of string with no vowels """
    result = [letter for letter in str.lower() if letter not in 'aeiou']
    return "".join(result)

class RemoveVowelsTest(unittest.TestCase):
    """ test remove_vowels function """
    def test_remove_vowels(self):
        self.assertEqual(remove_vowels('hello world'), 'hll wrld')
        self.assertEqual(remove_vowels('Python'), 'pythn')
        self.assertEqual(remove_vowels('I love Python'), ' lv pythn')
        self.assertEqual(remove_vowels(''), '')


"""
Part 2: Password Check
Write a function check_pwd(pwd) that takes a string as a parameter and returns True or False
if the password include at least one upper case character, at least one lower case character,
and the password must end with at least one digit.
"""
def check_pwd(pwd):
    [contains_lower, contains_upper] = [[char.islower() for char in pwd], [char.isupper() for char in pwd]]
    return any(contains_lower) and any(contains_upper) and pwd[len(pwd)-1].isdigit()

class CheckPwdTest(unittest.TestCase):
    """ test check_pwd function """
    def test_check_pwd(self):
        self.assertTrue(check_pwd('MingHui_2018'))
        self.assertFalse(check_pwd('minghui_2018'))
        self.assertFalse(check_pwd('MINGHUI_2018'))
        self.assertFalse(check_pwd('2018_minghui'))
        self.assertFalse(check_pwd(''))


"""
Part 3: Insertion Sort
Write a function insertion_sort(l) that returns a copy of the argument sorted 
using a list and the insertion sort algorithm discussed in class.

Method:
1. Create an empty list;
2. Iterate through each of the element in the list to be sorted;
3. For each element, iterate through the new sorted list from large to small for comparing.
4. Until find a number in the new sorted list smaller than the element, then insert the element next to it;
5. If no number is found to be smaller than the element, then insert the element as the start of the new sorted list.
"""
def insertion_sort(list):
    """ return a sorted list """
    result = []
    for element in list:
        for i in range(len(result)-1, -1, -1):
            if element >= result[i]:
                result.insert(i+1, element)
                break
        else:
            result.insert(0, element)
    return result

class InsertionSortTest(unittest.TestCase):
    """ test the insertion_sort function """
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([3, 1, 3, 5]), [1, 3, 3, 5])
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3 ,4, 5])
        self.assertEqual(insertion_sort([6, 3, 7, 3, 7, 2, 100]), [2, 3, 3, 6, 7, 7, 100])


"""
Part 4: Binary Tree
Write a BTree class to implement Binary Trees. And implement find, insert and traverse methods.
"""
class BTree:
    def __init__(self, value):
        """
        Create a new BTree with a single node with the specified value, no left child, and no
        right child.
        """
        if value is None:  # Make sure the tree contains some value
            raise ValueError('Error! None is not accepted.')

        if type(value) is str:
            raise TypeError('Error! Tree only accept numbers.')

        self.root = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        """
        Insert value as a new terminal node in the appropriate spot in self if value is not
        already in the BTree, or return None
        """
        if value is None:
            raise ValueError('Error! None is not accepted.')

        if type(value) is str:
            raise TypeError('Error! Tree only accept numbers.')

        if value == self.root:  # make sure the value is not already in the tree
            return None

        elif value < self.root:  # value less than root, then check the left subtree
            if self.left_child == None:
                self.left_child = BTree(value)
            else:
                self.left_child.insert(value)

        elif value > self.root:  # value less than root, then check the right subtree
            if self.right_child == None:
                self.right_child = BTree(value)
            else:
                self.right_child.insert(value)

    def find(self, value):
        """
        Return True if value is in the BTree or False.
        Same method as insert method.
        """
        if type(value) is str:
            raise TypeError('Error! Tree only accept numbers.')

        if value is None:
            return False

        if value == self.root:
            return True

        elif value < self.root:
            if self.left_child == None:
                return False
            return self.left_child.find(value)

        elif value > self.root:
            if self.right_child == None:
                return False
            return self.right_child.find(value)

    def traverse(self):
        """
        Traverse all of the nodes in BTree from smallest to largest
        return a list of values from each node.
        Note: this is pre-order traverse

        Note: If not using "traverse_list +=", this would wrongly clean the list every time call this method.
              Using += to store the value last time appended.

        Method:
        1. First traverse left subtree
        2. add node value into the new list
        3. Traverse the right subtree
        """
        traverse_list = []
        if self.left_child:
            traverse_list += self.left_child.traverse()

        traverse_list.append(self.root)

        if self.right_child:
            traverse_list += self.right_child.traverse()
        return traverse_list
    

class BTreeTest(unittest.TestCase):
    """ test that all binary tree methods work properly """
    def test_init(self):
        with self.assertRaises(ValueError):
            bt = BTree(None)
        with self.assertRaises(TypeError):
            bt2 = BTree('1')

    def test_find(self):
        bt = BTree(27)
        bt.insert(13)
        bt.insert(30)
        self.assertTrue(bt.find(27))
        self.assertTrue(bt.find(13))
        self.assertFalse(bt.find(99))
        self.assertFalse(bt.find(None))

        with self.assertRaises(TypeError):
            bt.find('13')

    def test_traverse(self):
        bt = BTree(27)
        bt.insert(13)
        bt.insert(30)
        bt.insert(1)
        bt.insert(26)
        bt.insert(15)
        bt.insert(10)
        self.assertEqual(bt.traverse(), [1, 10, 13, 15, 26, 27, 30])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

