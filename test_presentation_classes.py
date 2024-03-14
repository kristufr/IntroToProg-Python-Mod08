# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Test Presentation Class
# Desc: This assignment demonstrates using Modules
#       This module will contain the unit tests for the Presentation class
# Change Log: (Who, When, What)
#   C.Cipolla, 3/13/2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee


class TestIOClass(unittest.TestCase):
    """
    A collection of unit test functions to test the IO Class functions

    ChangeLog: (Who, When, What)
    - C.Cipolla, 3/13/2024, Created Class
    """

    # ******** test input menu ********
    def test_input_menu_choice(self):
        with patch("builtins.input", return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual('2', choice)

    def test_input_menu_choice_outofbounds(self):
        with patch("builtins.input", return_value=2345):
            choice = IO.input_menu_choice()
            self.assertRaises(Exception)

    # ******** test output data ********
    def test_output_data(self):
        # tbd
        pass

    # ******** test input data ********
    def test_input_data(self):
        with patch('builtins.input', side_effect=["Qwerty", "Smith", "2020-01-01", 1]):
            employees: list = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
        self.assertEqual(1, len(employees))
        self.assertEqual('Qwerty', employees[0].first_name)
        self.assertEqual('Smith', employees[0].last_name)
        self.assertEqual('2020-01-01', employees[0].review_date)
        self.assertEqual(1, employees[0].review_rating)

    def test_input_data_invalidinput(self):
        with patch('builtins.input', side_effect=["123", "Smith", "2020-01-01", 1]):
            employees: list = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
        self.assertEqual(0, len(employees))

        with patch('builtins.input', side_effect=["Qwerty", "345", "2020-01-01", 1]):
            employees: list = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
        self.assertEqual(0, len(employees))

        with patch('builtins.input', side_effect=["Qwerty", "Smith", "Jan 1st, 2020", 1]):
            employees: list = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
        self.assertEqual(0, len(employees))

        with patch('builtins.input', side_effect=["Qwerty", "Smith", "2020-01-01", 10]):
            employees: list = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
        self.assertEqual(0, len(employees))
if __name__ == '__main__':
    unittest.main()
