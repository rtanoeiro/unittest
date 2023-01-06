"""
Section 4 functions file
"""
import string

def counter(name: str = "") -> int:
    '''
    This function count the name of ascii letters in the given name
    '''

    name = name.strip()
    allowed_chars = [letter for letter in string.ascii_letters]
    name_bool = [False if letter in allowed_chars else True for letter in name]
    if any(name_bool):
        raise UnicodeError(f"There could be one or more non-english characters in the given name: \
{name}, please review the input name")
    elif name=="":
        raise Exception("The give name was empty, make sure to \
give a name with at least 1 character")
    elif name is None:
        raise Exception("Make sure to give a name with at least 1 character")

    return len(name)
