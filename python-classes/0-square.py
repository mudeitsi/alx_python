"""
This module defines a Square class to represent a square with a specific size.
The size of the square is maintained as a private attribute to ensure control over its value.
"""

class Square:
    """
    This class defines a square by its size, maintaining it as a private attribute.
    The size of the square is essential for various computations, such as area,
    and control over its value is maintained by keeping it private.
    """

    def __init__(self, size):
        """
        Initializes the Square class with the given size.
        :param size: The size of the square, no type/value verification is performed.
        """
        self.__size = size

