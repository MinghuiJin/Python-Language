"""
Homework 7:
Practice of datetime module, Files Analysis
"""

"""
Part 1: Date Arithmetic
"""
# print('***************** Date Arithmetic *****************')

import datetime

def date_time():
    # 1.1 What is the date three days after Feb 27, 2000?
    date1 = "Feb 27, 2000"
    dt1 = datetime.datetime.strptime(date1, '%b %d, %Y')
    date_1 = dt1 + datetime.timedelta(days = 3)
    print("The date three days after {} is {}".format(dt1.strftime('%Y-%m-%d'), date_1.strftime('%Y-%m-%d')) )

    # 1.2 What is the date three days after Feb 27, 2017?
    date2 = "Feb 27, 2017"
    dt2 = datetime.datetime.strptime(date2, '%b %d, %Y')
    date_2 = dt2 + datetime.timedelta(days = 3)
    print("The date three days after {} is {}".format(dt2.strftime('%Y-%m-%d'), date_2.strftime('%Y-%m-%d')) )

    # 1.3 How many days passed between Jan 1, 2017 and Oct 31, 2017?
    date3 = "Jan 1, 2007"
    date4 = "Oct 31, 2017"
    dt3 = datetime.datetime.strptime(date3, '%b %d, %Y')
    dt4 = datetime.datetime.strptime(date4, '%b %d, %Y')
    delta = dt4 - dt3
    print("{} days passed between {} and {}".format(delta.days, dt3.strftime('%Y-%m-%d'), dt4.strftime('%Y-%m-%d')))

"""
Part 2: Field separated file reader
Reading text files with a fixed number of fields, separated by a pre-defined character. 
Write a generator function to read text files and return all of the values on a single 
line on each call to next(). 
"""
# print('\n***************** File Reader *****************')

def file_reader(path, f_num = 2, sep = ',', header = False):
    """
    :param path: the file to be read
    :param f_num: the number of fields to be expected for each line, default by 2
    :param sep: to specify the field separator which defaults to comma
    :param header: to specify if the first line in the file is a header line, default by False
    :return:
    """
    try:
        fp = open(path)
    except FileNotFoundError:
        print("Can't open", path)
    else:
        line_num = 0
        with fp:
            for line in fp:
                line_num += 1
                try:
                    sep_line = tuple(line.strip('\n').split(sep))
                    if len(sep_line) != f_num: # verify whether the separated fields consistent with expected
                        raise ValueError

                except ValueError:
                    print("{} has {} fields on line {}, but expected {} fields.".format(path, len(sep_line), line_num, f_num))

                else:
                    if header == True: # skip the head row
                        header = False
                        continue
                    else:
                        yield sep_line

"""
Part 3: Scanning directories and files
Write a Python program that given a directory name, searches that directory for Python files 
(i.e. files ending with .py).  For each .py file, open each file and calculate a summary of 
the file.
"""
# print('\n***************** File Scanner *****************')

import os
from prettytable import PrettyTable

def files_scanner(path):
    """ return the information for all files under a directory and generate the table for them"""
    try:
        files = [file for file in os.listdir(path) if file.endswith('.py')] # get all python files

    except FileNotFoundError:
        print('{} cannot be found'.format(path))

    else:
        files_scanner = list() # store the information of files

        for f in files:
           file_name = os.path.join(path, f)
           files_scanner.append(file_analyser(file_name))

        pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])
        for file_name, classes, functions, lines, characters in files_scanner:
            pt.add_row([file_name, classes, functions, lines, characters])

        print(pt)
        return files_scanner

def file_analyser(file_name):
    """ return the information of a file """
    try:
        file = open(file_name, 'r')

    except FileNotFoundError:
        print('{} cannot be opened'.format(f))

    else:
        with file:
            characters = file.read() # read file into a buffer
            lines = characters.strip('\n').split('\n')

            functions = 0
            classes = 0
            for line in lines:
                if line.strip(' ').startswith('class '):
                    classes += 1
                elif line.strip(' ').startswith('def '):
                    functions += 1

        return [file_name, classes, functions, len(lines), len(characters)]


def main():
    date_time()

    path = "/Users/minghuijin/Desktop/student.csv"
    for i in file_reader(path, 3, ' ', header=True):
        print(i)

    path = "/Users/minghuijin/Desktop/student.csv"
    for i in file_reader(path, 3, ' '):
        print(i)

    dir = '/Users/minghuijin/Desktop'
    files_scanner(dir)

if __name__ == '__main__':
    main()
