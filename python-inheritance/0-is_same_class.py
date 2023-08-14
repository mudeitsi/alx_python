def is_same_class(obj, a_class):
    """Determine if an object is exactly an instance of a specified class

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is exactly an instance of the specified class; otherwise False.
    """
    return type(obj) is a_class

