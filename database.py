#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 21:59:54 2018

@author: minghui jin
"""
""" 
Implementing a repository to store all the information for students and instructors.
The unique info(primary key) for each person is the CWID.
To specify the info in grades.txt, use CWID to look up info for each person.

All the students info is stored in a dictionary, where the key is CWID, the value is an instance is Student.
All the instructors info is stored in a dictionary, where the key is CWID, the value is an instance is Instructor.
"""
import os
from person import Student, Instructor
from prettytable import PrettyTable

class Repository:
    """ Store all the information for all students and instructors """
    def __init__(self, dir_path):
        """ Specifies a directory path where to find the students.txt, instructors.txt, and grades.txt files """
        self.students_path = os.path.join(dir_path, 'students.txt')
        self.instructors_path = os.path.join(dir_path, 'instructors.txt')
        self.grades_path = os.path.join(dir_path, 'grades.txt')
        
        self.students = dict() # initialize the students DB
        self.instructors = dict() # initialize the instructors DB
        
        """ run methods to generate students DB and instructors DB and print the table of them """
        self.students_DB()
        self.instructors_DB()
        self.grades_DB()
        self.print_student_table()
        self.print_instructor_table()
        
    def file_reader(self, file_path):
        """ a generator to read file line by line """
        try:
            file = open(file_path,'r')
        except FileNotFoundError as e:
            print('Error! Cannot open file {}'.format(file_path))
        else:
            with file:
                for line in file:
                    yield line.strip().split('\t')
        
    def students_DB(self):
        """ Structure: CWID, Name, Major
            reading in the students.txt file line by line, updating the basic info for one student """
        for person_info in self.file_reader(self.students_path):
            self.students[person_info[0]] = Student(person_info)
        
    def instructors_DB(self):
        """ Structure: CWID, Name, Department
            reading in the instructorss.txt file line by line, updating the basic info for one instructor """
        for person_info in self.file_reader(self.instructors_path):
            self.instructors[person_info[0]] = Instructor(person_info)
    
    def grades_DB(self):
        """ Structure: CWID_student, Course, Grade, CWID_instructor """
        for grades_info in self.file_reader(self.grades_path):
            CWID_stu, course, grade, CWID_ins = grades_info
            
            if CWID_stu not in self.students.keys(): # course info in grades.txt but no corresponding student is found
                raise ValueError('Student CWID {} is not in the student system.'.format(CWID_stu))
            
            if CWID_ins not in self.instructors.keys(): # course info in grades.txt but no corresponding instructor is found
                raise ValueError('Instructor CWID {} is not in the instructor system.'.format(CWID_stu))
            
            self.students[CWID_stu].add_course(course, grade) # add a course and grade to the student containers
            self.instructors[CWID_ins].add_course(course) # add a course and increment the number of students by 1 to the instructor containers
    
    def print_student_table(self):
        """ generate the prettytable for students summary """
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Major', 'Courses'])
        for person in self.students.values():
            pt.add_row(person.get_student_info())
        print(pt)
        
    def print_instructor_table(self):
        """ generate the prettytable for instructors summary """
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Department', 'Courses', 'Student Num'])
        for person in self.instructors.values():
            for item in person.get_instructor_info():
                pt.add_row(item)
        print(pt)

def main():
    dir_path = '/Users/minghuijin/Desktop/Stevens'
    stevens = Repository(dir_path)

if __name__ == '__main__':
    main()