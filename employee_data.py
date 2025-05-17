# the program asks for employee data input, displays employee data list or raises the exceptions
# input: y/n answer for displaying the data list
# output: displays employee data list


class EmployeeData:
    def __init__(self, data):
        self.data = data

    def return_employee_data(self):
        for employee in employee_data:
            print(
                f'{employee["name"]}, {employee["surname"]}, Pracovné zaradenie: {employee["job_classification"]}, '
                f'Príspevok: {employee["contribution_amount_gross"]}, Príspevok po zdanení: {employee["contribution_amount_net"]}'
            )

    def show_data(self):
        try:
            show_employees = input("Zobraziť zoznam zamestnancov (a/n): ").strip().lower()

            if show_employees not in ["a","n"]:
                raise ValueError ("Nespravny údaj. Zadajte iba 'a' alebo 'n'")

            if show_employees == "a":
                self.return_employee_data()
                return show_employees

            else:
                print("Čauko, koniec programu.")

        except ValueError as error:
            print("Nespravny údaj.", error)



employee_data = [
    {"name": "Asterix", "surname": "Galois", "job_classification": "Opatrovateľ", "contribution_amount_gross": 2000,
     "contribution_amount_net": 1620},
    {"name": "Obelix", "surname": "Gal", "job_classification": "Sociálny pracovník", "contribution_amount_gross": 1500,
     "contribution_amount_net": 1620},
    {"name": "Scoobee", "surname": "Doo", "job_classification": "Inštruktor sociálnej rehabilitácie",
     "contribution_amount_gross": 2000, "contribution_amount_net": 1215}
]

e = EmployeeData(employee_data)
e.show_data()

