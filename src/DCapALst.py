## @file DCapALst.py
#  @title Department Capacity Association List
#  @author Dominik Buszowiecki
#  @date February 9, 2019

from StdntAllocTypes import *


## @brief An abstract data type containing the capacities of engineering departments as a list
class DCapALst:

    s = []

    ## @brief Initializes the Department Capacity List to be empty
    @staticmethod
    def init():
        DCapALst.s = []

    ## @brief Adds a department and its capacity to the list
    #  @exception throws KeyError if the given department has been added before
    #  @param d A department of type StdntAllocTypes.DeptT
    #  @param n An integer representing the capacity of the department (d parameter)
    @staticmethod
    def add(d: DeptT, n: int):
        for i in DCapALst.s:
            if d == i[0]:
                raise KeyError
        DCapALst.s.append((d, n))

    ## @breif Removes a department and its capacity from the list
    #  @exception throws KeyError if the given department is not in DCapALst
    #  @param d A department of type StdntAllocTypes.DeptT to be removed
    @staticmethod
    def remove(d: DeptT):
        for i in range(0, len(DCapALst.s)):
            if d == DCapALst.s[i][0]:
                del DCapALst.s[i]
                return
        raise KeyError

    ## @brief elm checks if a department has been added
    #  @param d A department of type StdntAllocTypes.DeptT
    #  @return True if the department has been added, otherwise False
    @staticmethod
    def elm(d: DeptT) -> bool:
        for i in DCapALst.s:
            if d == i[0]:
                return True
        return False

    ## @brief capacity returns the capacity of a department
    #  @exception throws KeyError if the department given is not in DCapALst
    #  @param d A department of type StdntAllocTypes.DeptT
    #  @return An integer representing the capacity of the department given as a parameter.
    @staticmethod
    def capacity(d: DeptT) -> bool:
        for i in DCapALst.s:
            if d == i[0]:
                return i[1]
        raise KeyError
