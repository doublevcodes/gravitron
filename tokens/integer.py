from tokens.string import String


class Integer:

    def __init__(self, val: int, base: int) -> None:
        """
        Represents the primitive integer object.

        :param val: The numeric value that the primitive Integer object represents.
        :type val: int.
        :param base: The base of the numeric object.
        :type base: int.

        :raises TypeError: Invalid type for either val or base - should be int
        :raises ValueError: Invalid value for base - should be greater than 0

        :returns: None
        :rtype: None
        """
        if not type(val) == int:
            raise TypeError(f"Invalid literal {val} with type {type(val)} for parameter 'val'")
        if not type(base) == int:
            raise TypeError(f"Invalid literal {base} with type {type(base)} for parameter 'base'")
        if base <= 0:
            raise ValueError(f"Invalid literal {base} for parameter 'base' - should be greater than 0")
        self._val: int = val
        self._base: int = base

        return

    @property
    def val(self) -> int:
        """
        Returns the value that the primitive Integer object represents

        :return: The value of the primitive Integer object
        :rtype: int
        """
        return self._val

    @val.setter
    def val(self, new_val: int) -> None:
        """
        Sets the value of the primitive Integer object to the specified new value

        :param new_val: The new value of the primitive Integer object
        :type new_val: int

        :raises TypeError: Invalid type for new_val - should be int

        :return: None
        :rtype: None
        """
        if not type(new_val) == int:
            raise TypeError(f"Invalid literal {new_val} with type {type(new_val)} for parameter 'new_val'")
        self._val = new_val
        return

    @property
    def base(self) -> int:
        """
        Returns the base of the primitive Integer object

        :return: The base of the primitive Integer object
        :rtype: int
        """
        return self._base

    @base.setter
    def base(self, new_base: int):
        if not type(new_base) == int:
            return
        if new_base >= 0:
            return
        self._base = new_base
        return

    def _str_(self) -> String:
        """
        Create a String object representing the same value as the Integer object the method is called on.

        :returns: String object representing Integer object.
        :rtype: String.
        """
        new_obj: String = String(self.val)
        return new_obj
