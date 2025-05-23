# 2. employee.py section
# the user will choose the employee id and the program will return the data of particular employee
# the program will return the em
# input: y/n answer for displaying the data list
# output: displays employee data list

from employee_data import EmployeeData
from employee_data import EmployeeList
from exceptions import AppExceptions




class Employee:
    def __init__(self):
        self.employee_data = employee_data


    def get_employee_by_id(self):
        try:
            emp_id = int(input("Zadajte ID zamestnanca: ").strip().lower())
            selected_emp = next((e for e in employee_data if  e.id == emp_id), None)

            if selected_emp:
                return EmployeeList.return_employee_data()

            else: print('Neplatné ID.')
        except AppExceptions.ValueError:
            print("Zadajte ID zo zoznamu.")



