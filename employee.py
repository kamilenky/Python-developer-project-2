# 2. employee.py section
# the user will choose the employee id and the program will return the data of particular employee
# the program will return the em
# input: y/n answer for displaying the data list
# output: displays employee data list

from emplmployee_data import EmployeeData
from employee_data import EmployeeList
from exceptions import AppExceptions


class Employee:
    def __init__(self, employee):
        self.employee = employee

    def get_employee_by_id(self, employee_id):
        try:
            emp_id = int(input("Zadajte ID zamestnanca: ").strip().lower())
            selected_emp = next(e for e in employee_data if  e.id = emp_id, None)

            if selected_emp:
                EmployeeList.return_employee_data()

            else: print('Neplatné ID.')
        raise AppExceptions.ValueError("Zadajte ID zo zoznamu.!)




        for emp in self.employee:
            if id.employee_id == employee_id:
                return

    def show_emp_id(self):
        show_emp_id = int(input("Zadajte ID zamestnanca: ").strip().lower())

        if show_emp_id not in return_employee_data():
            raise AppExceptions.ValueError("Neplatné id")

        if show_emp_id == ...
            self.get_employee_by_id
            return show_emp_id



    def ReturnEmployeeName(self, employee_id):
        pass
        # get_id = input --> id / name
        # print()

    def