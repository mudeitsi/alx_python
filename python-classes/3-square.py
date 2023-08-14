"""This module defines a Square class to represent a geometric square with controlled size attribute and a method to calculate the area."""

class Square:
    """Square class defines a square by size with type and value control, and provides a method to calculate its area.
    
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

