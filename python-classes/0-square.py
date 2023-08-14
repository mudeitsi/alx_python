class Square:
    """
    This class defines a square by its size.
    The size attribute is private, as it is essential to the properties of the square.
    Control over the size attribute is maintained by keeping it private.
    """

    def __init__(self, size):
        """
        Initializes the Square class with a given size.
        :param size: The size of the square.
        """
        self.__size = size

