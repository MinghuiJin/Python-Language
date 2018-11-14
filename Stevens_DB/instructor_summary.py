import sqlite3
from prettytable import PrettyTable

DB_FILE = "stevens_db.db"
stevens_db = sqlite3.connect(DB_FILE)

query = """select CWID, Name, Dept, Course, count(Course)
            from instructors join grades
            on CWID = Instructor_CWID
            group by course, Instructor_CWID """

pt = PrettyTable(field_names = ['CWID', 'Name', 'Department', 'Course', 'Student Num'])

for row in stevens_db.execute(query):
    pt.add_row(row)

print(pt)