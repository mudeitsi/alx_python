"""This module defines a Square class to represent a geometric square with controlled size attribute and methods to calculate the area and print the square."""

class Square:
    """Square class defines a square by size with type and value control, and provides methods to calculate its area and print it.
    
    Attributes:
        size (int): Size of the square, must be an integer and >= 0.
    """
    
    def __init__(self, size=0):
        """Initialize Square with given size.
        
        Args:
            size (int, optional): Size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.
        
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.
        
        Args:
            value (int): New size of the square.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.
        
        Prints an empty line if size is equal to 0.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

