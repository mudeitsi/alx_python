#!/usr/bin/python3
class Square(Rectangle):
    """
    Class representing a Square, which inherits from the Rectangle class.
    """
    def __init__(self, size):
        """
        Initialize the Square object with the given size.

        Args:
            size: The length of the sides of the square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

