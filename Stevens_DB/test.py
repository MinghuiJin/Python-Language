#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 01:22:23 2018

@author: minghui jin
"""

import unittest
from database import Repository

class DBTest(unittest.TestCase):
    def test_stevens(self):
        """ test whole correct files """
        stevens = Repository('/Users/minghuijin/Desktop/Stevens')
        
        students_info = {'10103': ['10103', 'Baldwin, C', 'SFEN', {'SSW 567': 'A', 'SSW 564': 'A-', 'SSW 687': 'B', 'CS 501': 'B'}],
                         '10115': ['10115', 'Wyatt, X', 'SFEN', {'SSW 567': 'A', 'SSW 564': 'B+', 'SSW 687': 'A', 'CS 545': 'A'}],
                         '10172': ['10172', 'Forbes, I', 'SFEN', {'SSW 555': 'A', 'SSW 567': 'A-'}],
                         '10175': ['10175', 'Erickson, D', 'SFEN', {'SSW 567': 'A', 'SSW 564': 'A', 'SSW 687': 'B-'}],
                         '10183': ['10183', 'Chapman, O', 'SFEN', {'SSW 689': 'A'}],
                         '11399': ['11399', 'Cordova, I', 'SYEN', {'SSW 540': 'B'}],
                         '11461': ['11461', 'Wright, U', 'SYEN', {'SYS 800': 'A', 'SYS 750': 'A-', 'SYS 611': 'A'}],
                         '11658': ['11658', 'Kelly, P', 'SYEN', {'SSW 540': 'F'}],
                         '11714': ['11714', 'Morton, A', 'SYEN', {'SYS 611': 'A', 'SYS 645': 'C'}],
                         '11788': ['11788', 'Fuller, E', 'SYEN', {'SSW 540': 'A'}]}
       
        instructors_info = {'98765': ['98765', 'Einstein, A', 'SFEN', {'SSW 567': 4, 'SSW 540': 3}], 
                            '98764': ['98764', 'Feynman, R', 'SFEN', {'SSW 564': 3, 'SSW 687': 3, 'CS 501': 1, 'CS 545': 1}], 
                            '98763': ['98763', 'Newton, I', 'SFEN', {'SSW 555': 1, 'SSW 689': 1}], 
                            '98762': ['98762', 'Hawking, S', 'SYEN', {}], 
                            '98761': ['98761', 'Edison, A', 'SYEN', {}], 
                            '98760': ['98760', 'Darwin, C', 'SYEN', {'SYS 800': 1, 'SYS 750': 1, 'SYS 611': 2, 'SYS 645': 1}]}
        
        
        students_dic = dict()
        for CWID, person in stevens.students.items():
            students_dic[CWID] = person.get_whole_info()
            
        instructors_dic = dict()
        for CWID, person in stevens.instructors.items():
            instructors_dic[CWID] = person.get_whole_info()
        
        self.assertEqual(students_dic, students_info)
        self.assertEqual(instructors_dic, instructors_info)
        
    def missing_info(self):
        """ test missing info in instructors.txt """
        with self.assertRaises(ValueError):
            Repository('/Users/minghuijin/Desktop/missed_info')
    
    def missing_person(self):
        """ test no corresponding person is found based on grades.txt """
        with self.assertRaises(ValueError):
            Repository('/Users/minghuijin/Desktop/grade_person_not_match')

if __name__ == '__main__':
    unittest.main(exit = False, verbosity = 2)