## @file SeqADT.py
#  @title Sequence ADT
#  @author Dominik Buszowiecki
#  @date February 9, 2019


## @brief An abstract data type that represents a sequence of values
class SeqADT:

    ## @brief SeqADT constructor
    #  @details Initializes the state variables of SeqADT. The state variables are a list that
    #           is given as a parameter and a variable used to index the list
    #           (initialized to 0).
    #  @param x A list of values
    def __init__(self, x: list):
        self.__s = x
        self.__i = 0

    ## @brief start will reset the index state variable to 0
    def start(self):
        self.__i = 0

    ## @brief next will return the next value in the sequence
    #  @exception throws StopIteration if there is no more items in the sequence
    #  @return value of next item in the sequence
    def next(self):
        if self.__i >= len(self.__s):
            raise StopIteration
        self.__i += 1
        return self.__s[self.__i - 1]

    ## @breif end will check if there are more items in the sequence
    #  @return True if there are no more items in the sequence, otherwise False
    def end(self) -> bool:
        return self.__i >= len(self.__s)
