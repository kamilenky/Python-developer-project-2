# 1. the program asks for employee data input, displays employee data list, raises the exceptions
from employee_data import EmployeeData, EmployeeList
from exceptions import AppExceptions
from employee import Employee
from requirements import RequirementsProlongedTenure, RequirementsShortenedTenure, RequirementsList, RequirementsById
from datetime import datetime
from dataclasses import dataclass



# Section: Lists - employee_data.py




employee_data = [
    EmployeeData(id=1, name="Astérix", surname="Galois", job_classification="Opatrovateľ",
                 contribution_amount_gross=2000,
                 contribution_amount_net=1620, start_date=datetime(2025, 1,1)),
    EmployeeData(id=2, name="Obélix", surname="Gal", job_classification="Sociálny pracovník",
                 contribution_amount_gross=1500,
                 contribution_amount_net=1215, start_date=datetime(2025, 1,1)),
    EmployeeData(id=3, name="Scoobee", surname="Doo", job_classification="Inštruktor sociálnej rehabilitácie",
                 contribution_amount_gross=2000,
                 contribution_amount_net=1620, start_date=datetime(2025, 1,1))
]


# Section: User Interaction - show_employee.py

try:
    e = EmployeeList(employee_data)
    e.show_data()

except AppExceptions.InvalidInputError as error:
    print("Nesprávny údaj.", error)


# Section: User Interaction - employee.py

g = Employee(employee_data)
g.get_employee_by_id()


# Section: Lists - requirements.py

reasons_1 = [
    RequirementsProlongedTenure(id=1, prolonged_tenure="ospravedlnená neprítomnosť zamestnanca"),
    RequirementsProlongedTenure(id=2, prolonged_tenure="výkon mimoriadnej služby")
]


reasons_2 = [
    RequirementsShortenedTenure(id=1, shortened_tenure="zamestnanec je preradený na inú pracovnú pozíciu"),
    RequirementsShortenedTenure(id=2, shortened_tenure="okamžité skončenie pracovného pomeru zamestnávateľom")
]

#Section: User Interaction - requirements.py

req_1 = RequirementsList(reasons_1)
req_2 = RequirementsList(reasons_2)

prolonged = req_1.show_requirements("\nZobraziť dôvody na predĺženie zmluvy?: ")
shortened = req_2.show_requirements("\nZobraziť dôvody na skrátenie zmluvy?: ")


if prolonged == "n" and shortened == "n":
    print("...")
else:
    if prolonged == "a":
        r_choice_1 = RequirementsById(reasons_1)
        r_choice_1.get_requirements_by_id("\nVyberte podmienku na predĺženie zmluvy: ")

    if shortened == "a":
        r_choice_2 = RequirementsById(reasons_2)
        r_choice_2.get_requirements_by_id("\nVyberte podmienku na skrátenie zmluvy: ")