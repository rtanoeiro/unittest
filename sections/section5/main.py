"""
This class is used to count numbers
"""


class Counter:
    """
    Counter Class where the lowest possible value is 0
    """

    def __init__(self) -> None:
        self._value = 0

    def add(self):
        """
        This function is going to add values to the initial value of the object
        """
        self._value += 1

    def remove(self):
        """
        This function is going to subtract values to the initial value of the object
        """
        if self._value == 0:
            self._value = 0
        else:
            self._value -= 1

    def clear(self):
        """
        This function is going reset the current value of the object
        """
        self._value = 0

    def get_value(self):
        """
        This function is get the current value of the object
        """
        return self._value
