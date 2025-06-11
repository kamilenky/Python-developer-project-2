# 2. employee.py section
# the user will choose the employee id and the program will return the data of particular employee
# input: y/n answer for displaying the data list
# output: displays employee data list

# from employee_data import EmployeeList
# from exceptions import AppExceptions


def greet():
    print("test main.py - employee")

# class EmployeeData:
#     def __init__(self, id, name, surname, job_classification, contribution_amount_gross, contribution_amount_net,
#                  start_date):
#         self.id = id
#         self.name = name
#         self.surname = surname
#         self.job_classification = job_classification
#         self.contribution_amount_gross = contribution_amount_gross
#         self.contribution_amount_net = contribution_amount_net
#         self.start_date = start_date
#         # self.end_date =  self.start_date.replace(year=self.start_date.year + 3)
#
#     def __str__(self):
#         return (f'Zamestnanec: {self.id},{self.name} {self.surname}, Pracovné zaradenie: {self.job_classification},'
#                 f'Príspevok: {self.contribution_amount_gross}, Príspevok po zdanení: {self.contribution_amount_net}, Začiatok zmluvy: {self.start_date.strftime("%d-%m-%y")}')
#
#
#     def to_dict(self):
#         return {"ID": self.id,
#                 "Meno": self.name,
#                 "Priezvisko": self.surname,
#                 "Pracovné zaradenie":self.job_classification,
#                 "Príspevok": self.contribution_amount_gross,
#                 "Príspevok po zdanení": self.contribution_amount_net,
#                 "Začiatok zmluvy": self.start_date.strftime("%d-%m-%y")
#         }
#
#
#
# class EmployeeManager:
#     def __init__(self, employee_list):
#         self.employee_list = employee_list
#
#     def return_employee_data(self):
#         for employee in self.employee_list:
#             print(employee)
#
#     def show_data(self):
#
#         show_employees = input("Zobraziť zoznam zamestnancov (a/n): ").strip().lower()
#
#         if show_employees not in ["a", "n"]:
#             raise AppExceptions.InvalidInputError("Zadajte iba 'a' alebo 'n'")
#
#         if show_employees == "a":
#             self.return_employee_data()
#             return show_employees
#
#         else:
#             print("...")
#
#     def get_employee_by_id(self):
#         try:
#             emp_id = int(input("Zadajte ID zamestnanca. Zadajte číslo: ").strip().lower())
#             selected_emp = next((e for e in self.employee_data if  e.id == emp_id), None)
#
#             if selected_emp:
#                 print(f"{selected_emp}")
#                 return selected_emp
#
#             else: print('Neplatné ID.')
#         except AppExceptions.ValueError:
#             print("Zadajte ID zo zoznamu.")
#
#
# # class Employee:
# #     def __init__(self, employee_data):
# #         self.employee_data = employee_data
#
#
#
#
#
