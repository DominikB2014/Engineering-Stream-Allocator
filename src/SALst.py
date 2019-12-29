## @file SALst.py
#  @title Student Association List
#  @author Dominik Buszowiecki
#  @date February 9, 2019

from StdntAllocTypes import *
from AALst import *
from DCapALst import *
from typing import Callable, List, Tuple


## @brief An abstract data type of all first year engineerng students
class SALst:

    s: List[Tuple[str, SInfoT]] = []

    ## @brief init initializes the list of students to be empty
    @staticmethod
    def init():
        SALst.s = []

    ## @brief Adds a student into the SALst
    #  @exception throws KeyError if the student given has been added before
    #  @param m A string of a student's macid
    #  @param i Information of a student given with the data type StdntAllocTypes.SInfoT
    @staticmethod
    def add(m: str, i: SInfoT):
        for student in SALst.s:
            if student[0] == m:
                raise KeyError
        SALst.s.append((m, i))

    ## @brief Removes a student from the SALst
    #  @exception throws KeyError if a student to be removed is not found
    #  @param m A string of a student's macid
    @staticmethod
    def remove(m: str):
        for i in range(0, len(SALst.s)):
            if SALst.s[i][0] == m:
                del SALst.s[i]
                return
        raise KeyError

    ## @brief elm checks if a student is already in the SALst
    #  @param m A string of a student's macid
    #  @return True if a student is in SALst, otherwise False
    @staticmethod
    def elm(m: str):
        for student in SALst.s:
            if student[0] == m:
                return True
        return False

    ## @brief returns the information assoaciated with a student
    #  @exception throws KeyError if the student is not found
    #  @param m A string of a student's macid
    #  @return A students information with the type StdntAllocTypes.SInfoT
    @staticmethod
    def info(m: str) -> SInfoT:
        for student in SALst.s:
            if student[0] == m:
                return student[1]
        raise KeyError

    ## @brief Sorts a subset of students based on GPA
    #  @details The method is given a function that is able to filter a student. The filter
    #           function takes in a student (SInfoT) and returns True if they pass the filter.
    #           The method will return a list of macids that passed the filter, sorted by
    #           their GPA in descending order.
    #  @param f A filtering function that returns a boolean
    #  @return A list of strings (each string is a macid) sorted by their GPA in
    #          descending order
    @staticmethod
    def sort(f: Callable[[SInfoT], bool]) -> list:
        temp_l = []
        for student in SALst.s:
            if f(student[1]):
                temp_l.append(student)
        temp_l = sorted(temp_l, key=lambda gpa_student: gpa_student[1].gpa, reverse=True)
        sorted_list = []
        for i in temp_l:
            sorted_list.append(i[0])
        return sorted_list

    ## @brief Computes the average of a particular subset of students
    #  @details The method is given a function that is able to filter a student. The function
    #           takes in a student(SInfoT) and returns True if they pass the filter. The
    #           method will then compute the average GPA amongst students who passed the
    #           filter.
    #  @exception throws ValueError if there are no students that pass the filter function.
    #  @param f A filtering function that returns a boolean
    #  @return A float representing the average GPA amongst a subset of students
    @staticmethod
    def average(f: Callable[[SInfoT], bool]) -> float:
        i = 0
        size = 0
        for student in SALst.s:
            if f(student[1]):
                i += student[1].gpa
                size += 1
        if size == 0:
            raise ValueError
        else:
            return i / size

    ## @breif Allocates students in SALst into their program
    #  @details Students are allocated into a department in AALst.
    #  Students with free choice are allocated first. The remaining students are allocated in
    #  a order based on their GPA, a student is allocated into their highest preferred choice
    #  that is not full in capacity.
    #  @exception throws RuntimeError if all of a student's choices are full.
    @staticmethod
    def allocate():
        AALst.init()
        f = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for student in f:
            ch = SALst.info(student).choices
            AALst.add_stdnt(ch.next(), student)

        s = SALst.sort(lambda t: not t.freechoice and t.gpa >= 4.0)
        for m in s:
            ch = SALst.info(m).choices
            alloc = False
            while not alloc and not ch.end():
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not alloc:
                raise RuntimeError
