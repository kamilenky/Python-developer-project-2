# 1. the program asks for employee data input, displays employee data list, raises the exceptions
from employee_data import EmployeeData
from employee_data import EmployeeList
from exceptions import AppExceptions
from employee import Employee


class List:
    def __init__(self):

    employee_data = [
        EmployeeData(id=1, name="Astérix", surname="Galois", job_classification="Opatrovateľ",
                     contribution_amount_gross=2000,
                     contribution_amount_net=1620),
        EmployeeData(id=2, name="Obélix", surname="Gal", job_classification="Sociálny pracovník",
                     contribution_amount_gross=1500,
                     contribution_amount_net=1215),
        EmployeeData(id=3, name="Scoobee", surname="Doo", job_classification="Inštruktor sociálnej rehabilitácie",
                     contribution_amount_gross=2000,
                     contribution_amount_net=1620)
        ]
# exceptions for employee_data.py section

try:
    e = EmployeeList(employee_data)
    e.show_data()

except AppExceptions.InvalidInputError as error:
    print("Nesprávny údaj.", error)


g = Employee(employee_data)
g.get_employee_by_id()
