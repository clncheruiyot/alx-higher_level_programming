#!/usr/bin/python3
# 0-square.py by Collins Bett
"""A module the define square """


class Square:
    """A class represent square"""

    def __init__(self, size=0):
        """Initialize the square class
        Args:
            size: represnet size of the square define
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieve size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square size
        """

        return (self.__size ** 2)

    def my_print(self):
        """prints square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
