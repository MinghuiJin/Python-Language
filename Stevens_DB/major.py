"""
Implementing the Major class that stores all information about a major including the
name of the major, the required courses and electives.

Flag = 'R' --> required course
Flag = 'E' --> elective course

Also compute remaining required and elective courses for students.
"""
class Major:
    """
    Store information about all majors.
    Major, Required course, Electives
    """
    def __init__(self, major):
        """ instance attributes: major, required courses, elective courses"""
        self.major = major

        self.required = set()
        self.elective = set()

    def update_major(self, flag, course):
        """ update the required courses('R') and the electives('E') """
        if flag == 'R':
            self.required.add(course)
        elif flag == 'E':
            self.elective.add(course)
        else:
            raise ValueError("Error! Unknown course flag!")

    def get_major_info(self):
        """ return the info for prettytable"""
        return [self.major, sorted(list(self.required)), sorted(list(self.elective))]

    def update_courses_info(self, courses):
        """ calculate the successfully completed courses, remaining required, elective courses"""
        passed_grades = ('A', 'A-', 'B+', 'B', 'B-', 'C+', 'C') # the grades needed to pass the course

        completed_courses = set()
        for course, grade in courses.items():
            if grade == ' ': # in case there is no grade for the course yet
                continue
            elif grade in passed_grades:
                completed_courses.add(course)

        remaining_required = self.left_required(completed_courses)
        remaining_electives = self.left_electives(completed_courses)

        return [sorted(list(completed_courses)), remaining_required, remaining_electives]

    def left_required(self, courses):
        """ return remaining required courses """
        if self.required.difference(courses) == set(): # no required course left
            return None
        else:
            return sorted(list(self.required.difference(courses)))

    def left_electives(self, courses):
        """ return remaining electives """
        left_courses = self.elective.difference(courses)
        if len(left_courses) < len(self.elective): # at least one elective course is needed
            return None
        else: # no elective courses has been completed
            return sorted(list(self.elective))

    def get_whole_info(self):
        """ return all info for the major """
        return [self.major, self.required, self.elective]
