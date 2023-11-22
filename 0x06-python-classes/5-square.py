#!/usr/bin/python3
class Square:
    """Represent a square."""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    @size.setter
    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def size(self):
        return self.__size

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
