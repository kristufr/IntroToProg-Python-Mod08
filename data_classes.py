# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Data Classes
# Desc: This assignment demonstrates using Modules
#       This module will contain the data classes
# Change Log: (Who, When, What)
#   C.Cipolla, 3/13/2024,Created Script
# ------------------------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("\n\t  * Please use the main.py file to start this application.")
    else:
        from datetime import date  # This will only import if the exception is not thrown.
except Exception as e:
    print(e.__str__())
    exit()
# from datetime import date


class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    - C.Cipolla, 3/13/2024, Modified into its own module
    """

    # Constructor
    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    # First name getter
    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        return self.__first_name.title()

    # First name setter: Letters Only
    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value.title()
        else:
            raise ValueError("The first name should only contain letters.")

    # last name getter
    @property
    def last_name(self):
        return self.__last_name.title()

    # last name setter: Letters Only
    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should only contain letters.")

    # String override
    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data (date?) of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    - C.Cipolla, 3/13/2024, Modified into its own module
    """

    # Constructor
    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01",
                 review_rating: int = 3):

        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    # review date getter
    @property
    def review_date(self):
        return self.__review_date

    # review date setter: ISO format
    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    # review rating getter
    @property
    def review_rating(self):
        return self.__review_rating

    # review rating setter: 1-5 only
    @review_rating.setter
    def review_rating(self, value: str):
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")

    # string override
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"
