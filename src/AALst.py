## @file AALst.py
#  @title Allocation Association List Module
#  @author Dominik Buszowiecki
#  @date February 9, 2019

from StdntAllocTypes import *


## @brief An abstract data type containing engineering departments and the students allocated
#         into them
class AALst:

    ## @brief Initiazlies the AALst
    #  @details The list is initialized with each department and an empty list of students for
    #   each department.
    @staticmethod
    def init():
        AALst.s = []
        for i in DeptT:
            AALst.s.append((i, []))

    ## @details add_stdnt adds a student to a specific department
    #  @param dep A department of type StdntAllocTypes.DeptT
    #  @param m A string representing the students macid
    @staticmethod
    def add_stdnt(dep: DeptT, m: str):
        for i in AALst.s:
            if i[0] == dep:
                i[1].append(m)

    ## @details lst_alloc returns a list of students in a specific department
    #  @param d A department of type  StdntAllocTypes.DeptT
    #  @return A list of strings where each string is a macid
    @staticmethod
    def lst_alloc(d: DeptT) -> list:
        for i in AALst.s:
            if i[0] == d:
                return i[1]

    ## @details num_alloc returns the number of students in a department
    #  @param d A department of type  StdntAllocTypes.DeptT
    #  @return A integer representing the number of students in a department
    @staticmethod
    def num_alloc(d: DeptT) -> int:
        for i in AALst.s:
            if i[0] == d:
                return len(i[1])
