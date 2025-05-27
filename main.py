# 1. the program asks for employee data input, displays employee data list, raises the exceptions
from employee_data import EmployeeData, EmployeeList
from exceptions import AppExceptions
from employee import Employee
from requirements import RequirementsProlongedTenure, RequirementsShortenedTenure, RequirementsList



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


reasons_1 = [
    RequirementsProlongedTenure(id=1, prolonged_tenure="ospravedlnená neprítomnosť zamestnanca"),
    RequirementsProlongedTenure(id=2, prolonged_tenure="výkon mimoriadnej služby")
]


reasons_2 = [
    RequirementsShortenedTenure(id=1, shortened_tenure="zamestnanec je preradený na inú pracovnú pozíciu"),
    RequirementsShortenedTenure(id=2, shortened_tenure="okamžité skončenie pracovného pomeru zamestnávateľom")
]


# exceptions for employee_data.py section

try:
    e = EmployeeList(employee_data)
    e.show_data()

except AppExceptions.InvalidInputError as error:
    print("Nesprávny údaj.", error)


g = Employee(employee_data)
g.get_employee_by_id()


# requirements.py section
req_1 = RequirementsList(reasons_1)
req_2 = RequirementsList(reasons_2)
req_1.show_requirements()
req_2.show_requirements()
