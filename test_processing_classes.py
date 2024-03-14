# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Test Processing Class
# Desc: This assignment demonstrates using Modules
#       This module will contain the unit tests for the Processing class
# Change Log: (Who, When, What)
#   C.Cipolla, 3/13/2024,Created Script
# ------------------------------------------------------------------------------------------------- #
import tempfile
import unittest
import json
from data_classes import Employee
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):
    """
    A collection of unit test functions to test the FileProcessor Class functions

    ChangeLog: (Who, When, What)
    - C.Cipolla, 3/13/2024, Created Class
    """

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employees: list = []  # so I can use it in all the functions

    def tearDown(self):
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        sampledata = [
            {"FirstName": "Qwerty", "LastName": "Jones", "ReviewDate": "2020-12-23", "ReviewRating": 3},
            {"FirstName": "Nevia", "LastName": "Iena", "ReviewDate": "2023-02-12", "ReviewRating": 4}
        ]
        with open(self.temp_file_name, 'w') as file:
            json.dump(sampledata, file)

        employees = FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name,
                                                               employee_data=self.employees, employee_type=Employee)

        self.assertEqual(len(sampledata), len(employees))

        self.assertEqual(sampledata[0]["FirstName"], employees[0].first_name)
        self.assertEqual(sampledata[0]["LastName"], employees[0].last_name)
        self.assertEqual(sampledata[0]["ReviewDate"], employees[0].review_date)
        self.assertEqual(sampledata[0]["ReviewRating"], employees[0].review_rating)

        self.assertEqual(sampledata[1]["FirstName"], employees[1].first_name)
        self.assertEqual(sampledata[1]["LastName"], employees[1].last_name)
        self.assertEqual(sampledata[1]["ReviewDate"], employees[1].review_date)
        self.assertEqual(sampledata[1]["ReviewRating"], employees[1].review_rating)

    def test_read_employee_data_from_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            employees = FileProcessor.read_employee_data_from_file(file_name="fakefile.json",
                                                                   employee_data=self.employees, employee_type=Employee)

    def test_write_employee_data_to_file(self):
        sampledata = [
            Employee("Qwerty", "Jones", "2020-12-23", 3),
            Employee("Nevia", "Iena", "2023-02-12", 4)
        ]
        # Run the function
        FileProcessor.write_employee_data_to_file(self.temp_file_name, employee_data=sampledata)

        # Read the file to see if it worked
        with open(self.temp_file_name, 'r') as file:
            employees = json.load(file)

        self.assertEqual(len(sampledata), len(employees))

        for i in range(len(sampledata)):
            self.assertEqual(sampledata[i].first_name, employees[i]["FirstName"])
            self.assertEqual(sampledata[i].last_name, employees[i]["LastName"])
            self.assertEqual(sampledata[i].review_date, employees[i]["ReviewDate"])
            self.assertEqual(sampledata[i].review_rating, employees[i]["ReviewRating"])


if __name__ == '__main__':
    unittest.main()
