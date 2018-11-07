"""
Homework 05

Practice of string and unittest.
"""
import unittest

"""
Part 1:
Write a function that  takes a string as an argument and returns a new 
string which is the reverse of the argument. Do not use Python's built in 
reverse function.
"""
def reverse(s):
    """ return the reverse of a string """
    if type(s) != str:  # without exception, then s would apply to any sequence
        raise TypeError("Error! The input must be a string!")

    rs = ""
    for i in s:
        rs  = i + rs  # Each character assert as the head of the reversed string
    return rs

class ReverseTest(unittest.TestCase):
    """ test reverse function """
    def test_reverse(self):
        """ verify that reverse function works properly """
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("123"), "321")
        self.assertEqual(reverse("abcdefg"), "gfedcba")
        with self.assertRaises(TypeError):
            reverse(['1', '2', '3'])


"""
Part 2:
Write a generator rev_enumerate(seq) that is similar to Python's built in enumerate(seq) 
generator but rather than starting at 0 and the first element in the sequence, start at 
the end of the sequence and return the elements in the sequence from last to first along 
with the corresponding offset.
"""
def rev_enumerate(seq):
    """ yield sequence's offset and element from end to start """
    for i in range(len(seq)):
        yield len(seq)-1-i, seq[len(seq)-1-i]


class RevEnumerateTest(unittest.TestCase):
    """ test rev_enumerate """
    def test_rev_enumerate(self):
        """ verify rev_enumerate works properly """
        seq1 = "Python" # string
        seq2 = ['P', 'y', 't', 'h', 'o', 'n'] # list
        seq3 = range(5) # a sequence of numbers
        seq4 = ('P', 'y', 't', 'h', 'o', 'n') # tuple
        self.assertTrue(list(rev_enumerate(seq1)) == list(enumerate(seq1))[::-1])
        self.assertTrue(list(rev_enumerate(seq2)) == list(enumerate(seq2))[::-1])
        self.assertTrue(list(rev_enumerate(seq3)) == list(enumerate(seq3))[::-1])
        self.assertTrue(list(rev_enumerate(seq4)) == list(enumerate(seq4))[::-1])


"""
Part 3:
Write a function find_second(s1, s2) that returns the offset of the second occurrence of
s1 in s2.  Return -1 if s1 does not occur twice in s2. 
"""
def find_second(s1, s2):
    """ return the offset of the second occurrence of target """
    if s1 == "" or s1 == None or s2 == "" or s2 == None:
        return -1

    occur = 0
    for offset, ele in enumerate(s2):
        if ele == s1[0]: # verify the first character is equal
            if s2[offset:offset+len(s1)] == s1: # then verify if the substring is equal to target
                occur += 1

        if occur == 2: # find two occurrence, then return the offset
            return offset
    return -1

class FindSecondTest(unittest.TestCase):
    """ test find_second """
    def test_find_second(self):
        """ verify that find_second works properly """
        self.assertTrue(find_second('iss','Mississippi') == 4)
        self.assertTrue(find_second('abba', 'abbabba') == 3)
        self.assertTrue(find_second('Miss', 'Mississippi') == -1)
        self.assertTrue(find_second('', 'Mississippi') == -1)
        self.assertTrue(find_second('iss', '') == -1)
        self.assertTrue(find_second('iss', 'Missississississsp') == 4)
        self.assertTrue(find_second('bab', 'abbabababab') == 4)


"""
Part 4:
Write a generator, get_lines(path), that opens a file for reading and returns one line 
from the file at a time. 
1. first combine lines that end with a backslash
2. remove all comments from the file where comments may begin with a '#' 

Method:
1. read the file into a list of lines, then deal the list by each element;
2. first determine whether the line is blank or only contains '\n';
3. Note: delete the '\n' for each line;
4. combine lines with backslash until a line with no backslash is found.
5. for new line that has already been combined, do delete_comment operation:
    I.  first determine is there is a comment in the line.
    II. if so, then yield line[:line.find('#')].
        Note: the '#' shall not be found as the head of the line, if so, then ignore the whole line.
    III. if there is no comment, then simply yield the line.
"""
def get_lines(path):
    """ yield lines after combination and comment delete """
    try:
        fp = open(path)
    except FileNotFoundError:
        print("File is not found!")
    else:
        with fp:
            lines = fp.readlines()

            s = "" # use the string for combining lines with backslash
            for line in lines:
                if line == None or line == '\n': # in case there are blank lines or the last line is blank
                    continue

                s += line.strip('\n') # delete line break

                if s[-1] != '\\': # determine whether the line ended with a backslash
                                  # no backslash at the end of line means line combination is completed
                    new_line = "".join(s.split('\\')) # split by '\' then create a new line

                    if '#' in new_line:  # determine whether the line contains a comment
                        pos = new_line.find('#')
                        if pos != 0:  # determine whether the whole line is a comment, if so, ignore this line
                            yield new_line[:pos]
                    else:
                        yield new_line

                    s = "" # Note: do not forget to clean the string


class GetLinesTest(unittest.TestCase):
    """ test get_lines """
    def test_get_lines(self):
        """ verify that get_lines works properly """
        path = '/Users/minghuijin/Desktop/hw05.txt'
        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        self.assertEqual(list(get_lines(path)), expect)


def main():
    path = '/Users/minghuijin/Desktop/hw05.txt'

    for line in get_lines(path):
        print(line)

if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)


