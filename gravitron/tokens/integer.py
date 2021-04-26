from gravitron.tokens.string import String
from gravitron.tokens.boolean import Boolean


class Integer:

    def __init__(self, val: int, base: int) -> None:
        """
        Represents the primitive Integer object.

        :param val: The numeric value that the primitive Integer object represents
        :type val: int
        :param base: The base of the numeric object
        :type base: int

        :raises TypeError: Invalid type for either val or base - should be int
        :raises ValueError: Invalid value for base - should be greater than 0

        :returns: None
        :rtype: None
        """
        if type(val) != int:
            raise TypeError(f"Invalid literal {val} with type '{val.__class__.__name__}' for parameter 'val'")
        if type(base) != int:
            raise TypeError(f"Invalid literal {base} with type '{base.__class__.__name__}' for parameter 'base'")
        if base <= 0:
            raise ValueError(f"Invalid literal {base} for parameter 'base' - should be greater than 0")
        self._val: int = val
        self._base: int = base
        return

    @property
    def val(self) -> int:
        """
        The value that the primitive Integer object represents.

        :returns: The value of the primitive Integer object
        :rtype: int
        """
        return self._val

    @val.setter
    def val(self, new_val: int) -> None:
        """
        Sets the value of the primitive Integer object to the specified new value
        making sure that the new value is an integer.

        :param new_val: The new value of the primitive Integer object
        :type new_val: int

        :raises TypeError: Invalid type for new_val - should be int

        :returns: None
        :rtype: None
        """
        if type(new_val) != int:
            raise TypeError(
                f"Invalid literal {new_val} with type '{new_val.__class__.__name__}' for parameter 'new_val'")
        self._val = new_val
        return

    @property
    def base(self) -> int:
        """
        The base of the primitive Integer object.

        :returns: The base of the primitive Integer object
        :rtype: int
        """
        return self._base

    @base.setter
    def base(self, new_base: int) -> None:
        """
        Sets the base of the primitive Integer object to the specified new base
        making sure that the new value is an integer and above 0.

        :param new_base: The new base of the primitive Integer object
        :type new_base: int

        :raises TypeError: Invalid type for new_base - should be int
        :raises ValueError: Invalid

        :returns: None
        :rtype: None
        """
        if type(new_base) != int:
            raise TypeError(
                f"Invalid literal {new_base} with type '{new_base.__class__.__name__}' for parameter 'new_base'")
        if new_base >= 0:
            raise ValueError(f"Invalid literal {new_base} with value '{new_base}' for parameter 'new_base")
        self._base = new_base
        return

    def _str_(self) -> String:
        """
        Creates a String object representing the same value as the primitive Integer object the method is called on.

        :returns: String object representing the primitive Integer object
        :rtype: String
        """
        new_obj: String = String(self.val)
        return new_obj

    def _bool_(self) -> Boolean:
        """
        Creates a Boolean object with the value 'True' or 'False'

        :returns: Boolean object representing the primitive Integer object
        :rtype: Boolean
        """
