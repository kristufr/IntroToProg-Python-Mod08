# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Test Presentation Class
# Desc: This assignment demonstrates using Modules
#       This module will contain the unit tests for the Presentation class
# Change Log: (Who, When, What)
#   C.Cipolla, 3/13/2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest


class TestPresentationClass(unittest.TestCase):
    """
    A collection of unit test functions to test the IO Class functions

    ChangeLog: (Who, When, What)
    - C.Cipolla, 3/13/2024, Created Class
    """

    def test_error_messages(self):
        # try message = "oops" -> assertEqual oops
        # try message = "oops" and e = "dadgum it broke" -> assertEqual oops & dadgum it broke
        pass

    # Don't need a test for output menu

    def test_input_menu_choice(self):
        # try 2 -> assertEqual 2
        # try 39838 -> with self.assertRaises(error)
        pass

    def test_output_data(self):
        # try employee = Employee("Alice", "Smith", "2020-01-01", 1)
        # assertEqual " Alice, Smith is rated as 1 (Not Meeting Expectations)"
        pass

    def test_input_data(self):
        # try employee = Employee("Alice", "Smith", "2020-01-01", 1)
        # use patch
        # employee_object = employee_type()
        # employee_object.first_name
        # employee_object.last_name
        # employee_object.review_date
        # employee_object.review_rating
        pass