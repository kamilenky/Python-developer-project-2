# 1. the section store the lists and calls other modules
# k tejto casti by som chela pridat aj volania z calculations.py, calculations.py je zatial jedina cast, ktora sa nevola z start.py
# program vyexportuje employee_data to CSV.Je to len skuska prace s csv, chcela by som aby sa v buducnosti importoval zoznam zamestnancov do listu/prip. prepisal list


from csv import DictWriter

from employee_data import EmployeeData, EmployeeList
from exceptions import AppExceptions
from employee import Employee
from requirements import RequirementsProlongedTenure, RequirementsShortenedTenure, RequirementsList, RequirementsById
from datetime import datetime, timedelta





# Section: Lists - employee_data.py


employee_data = [
    EmployeeData(id=1, name="Adam", surname="A", job_classification="Opatrovateľ",
                 contribution_amount_gross=2000,
                 contribution_amount_net=round(2000 * 0.81,2), start_date=datetime(2025, 1, 1)),
    EmployeeData(id=2, name="Braňo", surname="B", job_classification="Sociálny pracovník",
                 contribution_amount_gross=1500,
                 contribution_amount_net=round(1500 * 0.81,2), start_date=datetime(2025, 1, 1)),
    EmployeeData(id=3, name="Cyril", surname="C", job_classification="Inštruktor sociálnej rehabilitácie",
                 contribution_amount_gross=2000,
                 contribution_amount_net=round(2000 * 0.81,2), start_date=datetime(2025, 1, 1))
]

# Section: User Interaction - show_employee.py

try:
    e = EmployeeList(employee_data)
    e.show_data()

except AppExceptions.InvalidInputError as error:
    print("Nesprávny údaj.", error)


# Section: Export of EmployeeData to CSV
with open("../employees.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["ID", "Meno", "Priezvisko", "Pracovné zaradenie", "Príspevok", "Príspevok po zdanení", "Začiatok zmluvy"]
    writer = DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for emp in employee_data:
        writer.writerow(emp.to_dict())

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

# Section: User Interaction - requirements.py

req_1 = RequirementsList(reasons_1)
req_2 = RequirementsList(reasons_2)

prolonged = req_1.show_requirements("\nZobraziť dôvody na predĺženie zmluvy? (a/n): ")
shortened = req_2.show_requirements("\nZobraziť dôvody na skrátenie zmluvy? (a/n): ")

if prolonged == "n" and shortened == "n":
    print("...")
else:
    if prolonged == "a":
        r_choice_1 = RequirementsById(reasons_1)
        r_choice_1.get_requirements_by_id("\nVyberte podmienku na predĺženie zmluvy. Zadajte číslo: ")

    if shortened == "a":
        r_choice_2 = RequirementsById(reasons_2)
        r_choice_2.get_requirements_by_id("\nVyberte podmienku na skrátenie zmluvy. Zadajte číslo: ")




