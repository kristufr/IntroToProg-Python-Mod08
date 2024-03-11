# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Test Data Class
# Desc: This assignment demonstrates using Modules
#       This module will contain the unit tests for the data classes
# Change Log: (Who, When, What)
#   C.Cipolla, 3/13/2024,Created Script
# ------------------------------------------------------------------------------------------------- #
import unittest
from data_classes import Person
from data_classes import Employee


class TestPerson(unittest.TestCase):
    """
    A collection of unit test functions to test the Person and Student Classes

    ChangeLog: (Who, When, What)
    - C.Cipolla, 3/13/2024, Created Class
    """

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual("John", person.first_name)  # (Expected, Actual)
        self.assertEqual("Doe", person.last_name)  # (Expected, Actual)

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual("John,Doe", str(person))  # (Expected, Actual)


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith", "2020-01-01", 1)
        self.assertEqual("Alice", employee.first_name)  # (Expected, Actual)
        self.assertEqual("Smith", employee.last_name)  # (Expected, Actual)
        self.assertEqual("2020-01-01", employee.review_date)  # (Expected, Actual)
        self.assertEqual(1, employee.review_rating)  # (Expected, Actual)

    def test_employee_date_type(self):  # Test the gpa validation
        with self.assertRaises(ValueError):
            student = Employee("Bob", "Johnson", "invalid_date", 1)

    def test_employee_rating_type(self):  # Test the gpa validation
        with self.assertRaises(ValueError):
            student = Employee("Bob", "Johnson", "2020-02-02", 10000000000)

    def test_employee_str(self):
        student = Employee("Eve", "Brown", "2020-02-02", 1)  # Tests the __str__() magic method
        self.assertEqual("Eve,Brown,2020-02-02,1", str(student))  # (Expected, Actual)


if __name__ == '__main__':
    unittest.main()
