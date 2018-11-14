"""
Implementing the Students class and Instructor class storing the information for a single person.
Student structure: CWID, Name, Major, Courses
Instructor structure: CWID, Name, Department, Courses, Number of students
"""
from collections import defaultdict

class Student:
    """
    Stores information about a SINGLE student with all of the relevant information including:
    CWID, name, major, courses with corresponding grades.
    """
    def __init__(self, person_info, major_info):
        """ CWID: str; name: str; major: str; courses: defaultdict(str) """ 
        if len(person_info) == 2 or any([item.isspace() for item in person_info]) or '' in person_info:
            raise ValueError("Missing basic information of students!")
        
        self.CWID, self.name, self.major = person_info
        self.major_info = major_info # all major info including required and elective courses
        self.courses = defaultdict(str)
    
    def add_course(self, course, grade):
        """ Key: course, Value: grade
            Update courses each time finding a course info """
        self.courses[course] = grade
        
    #def compute_GPA(self):
        # further implementation
        
    def get_whole_info(self):
        """ return whole info of students including grades """
        return [self.CWID, self.name, self.major, self.courses] 
        
    def get_student_info(self):
        """ return the details for a single student in a list 
            Note: a student may just registered in the college having no course info """
        if not self.courses.items():
            return [self.CWID, self.name, self.major, None, None]
        else:
            return [self.CWID, self.name, self.major, sorted(list(self.courses.keys()))]
    

class Instructor:
    """
    Stores information about a single Instructor with all of the relevant information including:
    CWID, name, department, courses with corresponding students number
    """
    def __init__(self, person_info):
        """ CWID: str; name: str; department: str; courses: defaultdict(int) """ 
        if len(person_info) == 2 or any([item.isspace() for item in person_info]) or '' in person_info:
            raise ValueError("Missing basic information of instructors!")
            
        self.CWID, self.name, self.department = person_info
        self.courses = defaultdict(int)
        
    def add_course(self, course):
        """ Key: course, Value: nunber of students
            Update courses by adding 1 to its value each time found one person taking this course """
               
        self.courses[course] += 1
    
    def get_whole_info(self):
        """ return whole info of instructors """
        return [self.CWID, self.name, self.department, self.courses] 
    
    def get_instructor_info(self):
        """ return the details for a single instructor in a list
            Note: for one instructor, there might be several courses and he might have no course info """
        info = list()
        if not self.courses.items():
            info.append([self.CWID, self.name, self.department, None, None])
        else:
            for course, student_num in self.courses.items():
                info.append([self.CWID, self.name, self.department, course, student_num])
        return info
    

