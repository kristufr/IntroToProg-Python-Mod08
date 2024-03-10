# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Main Module
# Desc: This assignment demonstrates using Modules
#       This the main module used to run the program
# Change Log: (Who, When, What)
#   C.Cipolla, 3/13/2024,Created Script
# ------------------------------------------------------------------------------------------------- #


try:
    if __name__ == "__main__":
        import processing_classes as proc
        import presentation_classes as pres
        from data_classes import Employee
    else:
        raise Exception("main.py starts the application and should not be imported.")
except Exception as e:
    print(e.__str__())
    exit()

# Constant Declaration
FILE_NAME: str = "EmployeeRatings.json"
MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

# Variable Declaration
employees: list = []  # a table of employee data
menu_choice = ''

# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                            employee_data=employees,
                                                            employee_type=Employee)
# Note Employee is the class name (ignore the warning)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages("Unhandled Exception", e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees,
                                                    employee_type=Employee)
            # Note Employee is the class name (ignore the warning)

            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages("Unhandled Exception", e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages("Unhandled Exception", e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
