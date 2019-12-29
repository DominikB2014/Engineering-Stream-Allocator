## @file Read.py
#  @title Read
#  @author Dominik Buszowiecki
#  @date February 9, 2019

from StdntAllocTypes import *
from DCapALst import *
from SALst import *
import re


## @brief Loads students from a file into the SALst
#  @details Each line in the file represents a student.
#           The format of each line should be: \n
#         macid, firstname, lastname, gender, gpa, [choice1, choice2, ...], freechoice \n
#           where gpa is a real number, gender is either male or female
#           and freechoice is either True or False.
#  @param s A string representing the name of the file
def load_stdnt_data(s: str):
    stdnt_data = open(s, 'r')
    student_list = stdnt_data.read().splitlines()
    stdnt_data.close()

    SALst.init()
    for student in student_list:
        info_list = re.split(", \[|\], |, ", student)  # noqa: W605
        choices = []
        for i in range(5, len(info_list) - 1):
            choices.append(DeptT(info_list[i]))
        if info_list[-1] == "False":
            free_choice = False
        else:
            free_choice = True
        sinfo = SInfoT(info_list[1], info_list[2],  # Students fname and lname
                       GenT(info_list[3]),          # Students Gender
                       float(info_list[4]),         # Students GPA
                       SeqADT(choices),             # Students choices
                       free_choice)                 # Freechoice boolean
        SALst.add(info_list[0], sinfo)


## @brief Loads department capacities from a file into the DCapALst
#  @details Each line in the file represents a department.
#           The format of each line should be: \n
#           department_name, capacity \n
#           where capacity is an integer.
#  @param s A string representing the name of the file
def load_dcap_data(s: str):
    dept_capacity = open(s, 'r')
    department_list = dept_capacity.read().splitlines()
    dept_capacity.close()

    DCapALst.init()
    for department in department_list:
        dep_list = department.split(', ')
        DCapALst.add(DeptT(dep_list[0]), int(dep_list[1]))
