"""
Section 1 first file
"""


# def upper_name(name):
#     """
#     This function returnes the given name in upper characters
#     input: str
#     output: upper str
#     """
#     return name.upper()
# 
# if upper_name("Ramon") == "RAMON":
#     print("Success!")
# else:
#     print("Fail!")

def avg(list_numbers):
    """
    This function returnes the average of all given numbers
    input: str
    output: upper str
    """
    total = 0
    for num in list_numbers:
        total += num
    return total / len(list_numbers)
