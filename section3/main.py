"""
Section 1 first file
"""


def avg(list_numbers:list) -> float:
    """
    This function returnes the average of all given numbers
    input: str
    output: upper str
    """
    total = 0
    for num in list_numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            try:
                num = int(num)
            except TypeError("Wrong data input. Please make sure all values are numbers") as exc:
                raise exc
    return total / len(list_numbers)
