"""This module defines a Square class with controlled size attribute."""

class Square:
    """Square class defines a square by size with type and value control.
    
    Attributes:
        size (int): Size of the square, must be an integer and >= 0.
    """
    
    def __init__(self, size=0):
        """Initialize Square with given size.
        
        Args:
            size (int, optional): Size of the square. Defaults to 0.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

