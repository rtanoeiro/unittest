"""
This class is used to create profiles
"""

class Profile:
    """
    This class creates a profile for a person
    """
    def __init__(self, name: str, age: int, job: str) -> None:
        self._name = name
        self._age = age
        self._job = job

    def print_name(self):
        """
        Print the name of the profile
        """
        print(self._name)

    def print_age(self):
        """
        Print the age of the profile
        """
        print(self._age)

    def print_job(self):
        """
        Print the job of the profile
        """
        print(self._job)
