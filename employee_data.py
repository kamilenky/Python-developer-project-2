# 1. employee_data.py section
# the program asks for employee data input, displays employee data list or raises the exceptions
# input: y/n answer for displaying the data list
# output: displays employee data list

from exceptions import AppExceptions


class EmployeeData:
    def __init__(self, id, name, surname, job_classification, contribution_amount_gross, contribution_amount_net,
                 start_date):
        self.id = id
        self.name = name
        self.surname = surname
        self.job_classification = job_classification
        self.contribution_amount_gross = contribution_amount_gross
        self.contribution_amount_net = contribution_amount_net
        self.start_date = start_date
        self.date_str = date_str

    def __str__(self):
        date_str = self.start_date.strftime("%d-%m-%y") if self.start_date else "%Y-%m-%d"
        return (f'Zamestnanec: {self.id},{self.name} {self.surname}, Pracovné zaradenie: {self.job_classification},'
            f'Príspevok: {self.contribution_amount_gross}, Príspevok po zdanení: {self.contribution_amount_net}, Začiatok zmluvy: {self.date_str}')


class EmployeeList:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def return_employee_data(self):
        for employee in self.employee_list:
            print(employee)

    def show_data(self):

        show_employees = input("Zobraziť zoznam zamestnancov (a/n): ").strip().lower()

        if show_employees not in ["a", "n"]:
            raise AppExceptions.InvalidInputError("Zadajte iba 'a' alebo 'n'")

        if show_employees == "a":
            self.return_employee_data()
            return show_employees

        else:
            print("...")
