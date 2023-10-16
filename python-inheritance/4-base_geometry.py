#!/usr/bin/Python3

class BaseGeometry:
    """BaseGeometry Class"""

    def __dir__(self) -> None:
        """This will control inherited attribute access"""
        attributes = super().__dir__()
        return [
            attribute for attribute in attributes if attribute != "__init_subclass__"
        ]

    def area(self):
        raise Exception("area() is not implemented")
