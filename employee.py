# 2. employee.py section
# the user will choose the employee id and the program will return the data of particular employee
# the program will return the em
# input: y/n answer for displaying the data list
# output: displays employee data list

from employee_data import EmployeeData

class Employee:
    def __init__(self, employee):
        self.employee = employee

    def get_employee_by_id(self, employee_id):
        for emp in self.employee:
            if id.employee_id == employee_id:
                return emp

    def ReturnEmployeeName(self, employee_id):
        pass
        # get_id = input --> id / name
        # print()
