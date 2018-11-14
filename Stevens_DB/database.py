"""
Implementing a repository to store all the information for students and instructors.
The unique info(primary key) for each person is the CWID.
To specify the info in grades.txt, use CWID to look up info for each person.

All the students info is stored in a dictionary, where the key is CWID, the value is an instance is Student.
All the instructors info is stored in a dictionary, where the key is CWID, the value is an instance is Instructor.
All the majors info is stored in dictionary, where the key is major name, the value is an instance of Major
"""
import os
from major import Major
from person import Student, Instructor
from prettytable import PrettyTable

class Repository:
    """ Store all the information for all students and instructors """
    def __init__(self, dir_path):
        """ Specifies a directory path where to find the students.txt, instructors.txt, and grades.txt files """
        self.students_path = os.path.join(dir_path, 'students.txt')
        self.instructors_path = os.path.join(dir_path, 'instructors.txt')
        self.grades_path = os.path.join(dir_path, 'grades.txt')
        self.majors_path = os.path.join(dir_path, 'majors.txt')

        self.students = dict() # initialize the students DB, key is CWID, value is instance of Student
        self.instructors = dict() # initialize the instructors DB, key is CWID, value is instance of Instructor
        self.majors = dict() # key is major, value is instance of Major
        
        # run methods to generate majors DB, students DB and instructors DB and print the table of them
        self.majors_DB()
        self.students_DB()
        self.instructors_DB()
        self.grades_DB()

        self.print_major_table()
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
            reading in the students.txt file line by line, updating the basic info for one student
            also for each instance of students, passing in major info
        """
        for person_info in self.file_reader(self.students_path):
            CWID, name, major = person_info

            if major not in self.majors:
                raise ValueError('Error! Missing major {} information.'.format(major))

            if CWID not in self.students:
                self.students[CWID] = Student(person_info, self.majors[major])

    def instructors_DB(self):
        """ Structure: CWID, Name, Department
            reading in the instructors.txt file line by line, updating the basic info for one instructor
        """
        for person_info in self.file_reader(self.instructors_path):
            self.instructors[person_info[0]] = Instructor(person_info)
    
    def grades_DB(self):
        """ Structure: CWID_student, Course, Grade, CWID_instructor """
        for CWID_stu, course, grade, CWID_ins in self.file_reader(self.grades_path):
            if CWID_stu not in self.students.keys(): # course info in grades.txt but no corresponding student is found
                raise ValueError('Student CWID {} is not in the student system.'.format(CWID_stu))
            
            if CWID_ins not in self.instructors.keys(): # course info in grades.txt but no corresponding instructor is found
                raise ValueError('Instructor CWID {} is not in the instructor system.'.format(CWID_stu))
            
            self.students[CWID_stu].add_course(course, grade) # add a course and grade to the student containers
            self.instructors[CWID_ins].add_course(course) # add a course and increment the number of students by 1 to the instructor containers

    def majors_DB(self):
        """ Structure: Department, Flag, Course
            Method:
                If major is already in the dict, then ignore, just update info.
                As each time declare an instance, the required and electives would be an emplty set,
                this would avoid clean the set by mistake.
        """
        for major, flag, course in self.file_reader(self.majors_path):
            if major not in self.majors:
                self.majors[major] = Major(major)

            self.majors[major].update_major(flag, course)

    def print_student_table(self):
        """ generate the prettytable for students summary """
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives'])
        for person in self.students.values():
            # calculating remaining required and elective courses
            courses = self.majors[person.major].update_courses_info(person.courses)

            CWID, name, major, c = person.get_student_info()
            person_info = [CWID, name, major] #ignore the courses info
            for item in courses:
                person_info.append(item)

            pt.add_row(person_info)
        print('Students Summary')
        print(pt)
        
    def print_instructor_table(self):
        """ generate the prettytable for instructors summary """
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Department', 'Courses', 'Student Num'])
        for person in self.instructors.values():
            for item in person.get_instructor_info():
                pt.add_row(item)
        print('Instructors Summary')
        print(pt)

    def print_major_table(self):
        """ generate the prettytable for majors summary """
        pt = PrettyTable(field_names = ['Major', 'Required Courses', 'Electives'])
        for major in self.majors.values():
            pt.add_row(major.get_major_info())

        print('Majors Summary')
        print(pt)

def main():
    dir_path = '/Users/minghuijin/Desktop/Stevens'
    stevens = Repository(dir_path)

if __name__ == '__main__':
    main()