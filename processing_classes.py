# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Processing Class
# Desc: This assignment demonstrates using Modules
#       This module will contain the classes to read/write to a file
# Change Log: (Who, When, What)
#   C.Cipolla, 3/13/2024,Created Script
# ------------------------------------------------------------------------------------------------- #
from json import JSONDecodeError

try:
    if __name__ == "__main__":
        raise Exception("\n\t  * Please use the main.py file to start this application.")
    else:
        import json
        from data_classes import Employee  # This will only import if the exception is not thrown.
except Exception as e:
    print(e.__str__())
    exit()


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    - RRoot,1.1.2030,Created Class
    - C.Cipolla, 3/13/2024, Modified into its own module
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object) -> list[object]:
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        C.Cipolla, 3/13/2024, Modified as required to operate in this module

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: a reference to the Employee class
        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except JSONDecodeError as e:
            raise JSONDecodeError("JSON data in file isn\'t valid")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        C.Cipolla, 3/13/2024, Modified as required to operate in this module

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as err:
            raise Exception("There was a non-specific error!", err)

