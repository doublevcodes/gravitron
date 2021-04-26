
class Boolean:

    def __init__(self, val: bool) -> None:
        """
        Represents the primitive Boolean object.

        :param val: Either True or False
        :type val: bool

        :raises TypeError: Invalid type for val - should be bool

        :returns: None
        :rtype: None
        """
        if type(val) != bool:
            raise TypeError(f"Invalid literal {val} with type '{val.__class__.__name__}' for parameter 'val'")
        self._val: bool = val
        return

    @property
    def val(self) -> bool:
        """
        The value the primitive Boolean object represents.
        Either True or False

        :raises TypeError: Invalid type for new_val - should be bool

        :returns: The value of the primitive Integer object
        :rtype: bool
        """
        return self._val

    @val.setter
    def val(self, new_val: bool) -> None:
        """
        Sets the value of the primitive Boolean object to the specified new value
        making sure that the new value is a boolean.

        :param new_val: The new value of the primitive Boolean object
        :return:
        """
        if type(new_val) != bool:
            raise TypeError(f"Invalid literal {new_val} with type '{new_val.__class__.__name__}' for parameter 'new_val'")
