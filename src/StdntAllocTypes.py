## @file StdntAllocTypes.py
#  @title Student Allocation Types
#  @author Dominik Buszowiecki
#  @date February 9, 2019

from SeqADT import *
from enum import Enum
from typing import NamedTuple


## @breif An Enumerated type of possible genders
class GenT(Enum):
    male = "male"
    female = "female"


## @brief An Enumerated type of possible engineering departments
class DeptT(Enum):
    civil = "civil"
    chemical = "chemical"
    electrical = "electrical"
    mechanical = "mechanical"
    software = "software"
    materials = "materials"
    engphys = "engphys"


## @brief A NamedTuple used to represent a student
#  @details A student has a: first name, last name, gender (given as a GenT type), gpa,
#           sequence of departments(given as a SeqADT of DeptT's), and a boolean to represent
#           if they have free choice.
class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT
    freechoice: bool
