# the program asks for employee data input, displays employee data list or raises the exceptions
# input: y/n answer for displaying the data list
# output: displays employee data list


class EmployeeData:
    def __init__(self, id, name, surname, job_classification, contribution_amount_gross, contribution_amount_net):
        self.id = id
        self.name = name
        self.surname = surname
        self.job_classification = job_classification
        self.contribution_amount_gross = contribution_amount_gross
        self.contribution_amount_net = contribution_amount_net

    def __str__(self):
       return  (f'Zamestnanec: {self.id},{self.name} {self.surname}, Pracovné zaradenie: {self.job_classification}, '
                f'Príspevok: {self.contribution_amount_gross}, Príspevok po zdanení: {self.contribution_amount_net}')

class EmployeeList:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def return_employee_data(self):
        for employee in self.employee_list:
           print(employee)

    def show_data(self):
        try:
            show_employees = input("Zobraziť zoznam zamestnancov (a/n): ").strip().lower()

            if show_employees not in ["a","n"]:
                raise ValueError ("Zadajte iba 'a' alebo 'n'")

            if show_employees == "a":
                self.return_employee_data()
                return show_employees

            else:
                print("Čauko, koniec programu.")

        except ValueError as error:
            print("Nespravny údaj.", error)



employee_data = [
    EmployeeData(id=1, name="Asterix", surname= "Galois", job_classification="Opatrovateľ", contribution_amount_gross= 2000,
     contribution_amount_net= 1620),
    EmployeeData(id=2, name="Obelix", surname= "Gal", job_classification="Sociálny pracovník", contribution_amount_gross= 1500,
     contribution_amount_net= 1215),
    EmployeeData(id=3, name="Scoobee", surname= "Doo", job_classification="Inštruktor sociálnej rehabilitácie", contribution_amount_gross= 2000,
     contribution_amount_net= 1620)
]

e = EmployeeList(employee_data)
e.show_data()


