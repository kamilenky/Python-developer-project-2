# 1. the program asks for employee data input, displays employee data list, raises the exceptions
from employee_data import EmployeeData
from employee_data import EmployeeList
from exceptions import AppExceptions


employee_data = [
    EmployeeData(id=1, name="Asterix", surname= "Galois", job_classification="Opatrovateľ", contribution_amount_gross= 2000,
     contribution_amount_net= 1620),
    EmployeeData(id=2, name="Obelix", surname= "Gal", job_classification="Sociálny pracovník", contribution_amount_gross= 1500,
     contribution_amount_net= 1215),
    EmployeeData(id=3, name="Scoobee", surname= "Doo", job_classification="Inštruktor sociálnej rehabilitácie", contribution_amount_gross= 2000,
     contribution_amount_net= 1620)
]
# exceptions for employee_data.py section

try:
    e = EmployeeList(employee_data)
    e.show_data()

except AppExceptions.InvalidInputError as error:
    print("Nespravny údaj.", error)
