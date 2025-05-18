# # the program asks for employee data input, displays employee data list or raises the exceptions
# # input: y/n answer for displaying the data list
# # output: displays employee data list
#
# class EmployeeData:
#     def __init__(self, data):
#         self.data = data
#
#     def return_employee_data(self):
#         for employee in employee_data:
#             print(
#                 f'{employee["name"]}, {employee["surname"]}, Pracovné zaradenie: {employee["job_classification"]}, '
#                 f'Príspevok: {employee["contribution_amount_gross"]}, Príspevok po zdanení: {employee["contribution_amount_net"]}'
#             )
#
#     def show_data(self):
#         try:
#             show_employees = input("Zobraziť zoznam zamestnancov (a/n): ").strip().lower()
#
#             if show_employees not in ["a","n"]:
#                 raise ValueError ("Nespravny údaj. Zadajte iba 'a' alebo 'n'")
#
#             if show_employees == "a":
#                 self.return_employee_data()
#                 return show_employees
#
#             else:
#                 print("Čauko, koniec programu.")
#
#         except ValueError as error:
#             print("Nespravny údaj.", error)
#
#
#     # output: zobrazi  tabulku  zamestnancov
#
#
# employee_data = [
#     {"name": "Asterix", "surname": "Galois", "job_classification": "Opatrovateľ", "contribution_amount_gross": 2000,
#      "contribution_amount_net": 1620},
#     {"name": "Obelix", "surname": "Gal", "job_classification": "Sociálny pracovník", "contribution_amount_gross": 1500,
#      "contribution_amount_net": 1620},
#     {"name": "Scoobee", "surname": "Doo", "job_classification": "Inštruktor sociálnej rehabilitácie",
#      "contribution_amount_gross": 2000, "contribution_amount_net": 1215}
# ]
#
# e = EmployeeData(employee_data)
# e.show_data()

# program zobrai zamestnanca a riradene data: meno, priezvisko, pracovne zaradenie, pracovny uvazok, vyska prispevku v hrubom,
# vyska prispevku v cistom, zaciatok zmluvy, predpokladany koniec zmluvy

class Employee
    pass

    def choose_employee(self):
        pass

    def ReturnEmployeeName(self):
        pass
        # get_id = input --> id / name
        # print()



# amendement requirements
class Requirements:
    def __init__(self, reasons: list) -> None:
        self.reasons = reasons
        # zostavi list podmienok pre pre predlzenie zmluvy/skratenie zmluvy

    def get_list_of_requirements(self):
        pass
        # get_list_req = input --> print("Zobrazit zoznam podmienok pre vratenie prispevku?"
        # Y / N)
        # if yes --> zobrazi list podmienok
        # if no --> print("Vratit sa na tabulku zamestnancov?")
        # if yes - --> vrati sa na tabulku zamestnancov
        # if no - --> skonci program


# vyhodnoti vstupy pre zobrazenie podmienok


def list_requirements(self):
    reason in self.reasons:
    reason.set_reason()


# vypise vsetky podmienky pre skratenie a predlzenie doby zotrvania zamestnanca v pracovnom pomere

def choose_requirement(self):
    pass


# uzivatel vyberie podmienku

def print_reason(self) -> None:
    print(f"Dovod nepritomnosti je {self.prolonged_tenure}")
    # vypise podmienky pre skratenie a predlzenie doby zotrvania zamestnanca v pracovnom pomere


class JobTenureProlonged:
    def __init__(self, prolonged_tenure: str, days: int) -> None:
        self.prolonged_tenure = prolonged_tenure
        self.days = days

    def choose_reason(self):
        pass

    def add_days(self):
        pass


reasons_1 = [
    JobTenureProlonged(prolonged_tenure="ospravedlnená neprítomnosť zamestnanca"),
    JobTenureProlonged(prolonged_tenure="neospravedlnená neprítomnosť zamestnanca"),
    JobTenureProlonged(prolonged_tenure="výkon mimoriadnej služby"),
    JobTenureProlonged(prolonged_tenure="výkon väzby alebo nepodmienečného trestu odňatia slobody"),
    JobTenureShortened(shortened_tenure="zamestnanec je preradený na inú pracovnú pozíciu")
]


class JobTenureShortened:
    def __init__(self, shortened_tenure: str, days: int) -> None:
        self.shortened_tenure = shortened_tenure
        self.days = days


reasons_2 = [
    JobTenureShortened(shortened_tenure="zamestnanec je preradený na inú pracovnú pozíciu")
    JobTenureShortened(
        shortened_tenure="na žiadosť zamestnanca je zamestnancovi znížený jeho pracovný úväzok pod dohodnutý úväzok ")
    JobTenureShortened(shortened_tenure="okamžitého skončenia pracovného pomeru zamestnávateľom")
]


class RepaymentObligation
    pass


# vypise podmineky, kedy sa prispevok nekrati

reasons_3 = [...]


# requirements = Requirements(reasons=reasons)
# print(requirements)
# reasons.list_requirements()


# other

class ContractDates:
    pass


# vrati datum - zaciatok zmluvu
# vrati datum - ukoncenie zmluvy


class CalculateJobTenurePeriod:
    pass


# vypocita dlzku pavoneho pomeru v dnoch, vyhodnoti datum zaciatku a ukoncenia zmluvy, vyhodoti podmienky
# vrati rozdiel medzi dohodnutou dlzkou pracovneho pomeru a skutocnou dlzkou PP


class CalculateContributionAmount:
    pass

    # vrati cast stabilizacneho prispevku urcenu na vratenie zamestnavatelovi

    def set_in_gros(self):
        pass

    def set_in_net(self):
        pass

# class JobClassification:
#     def __init__(self, job_classification: str, working_hours: int) -> None:
#         self.job_classificaiton = job_classification
#         self.working_hours = working_hours
#         # priradi pracovne zaradenie zamestnancovi
#
#     def AssignJobClassification(self) -> None:
#         print(f"Pracovné zaradenienie: {self.job_classificaiton}")
#
#     def AssignWorkingHours(self) -> None:
#         print(f"Pracovný uväzok: {self.working_hours}")
#
#     def assign_contribution_rate(self):
#         full_contribution = 100
#         if job_classification=="Sociálny pracovník":
#             return full_contribution*1
#         elif job_classification=="Opatrovateľ":
#             return full_contribution*0.5
#
#
#
#
# job_title_1 = JobClassification(job_classification="Sociálny pracovník", working_hours=40)
# job_title_2 = JobClassification(job_classification="Opatrovateľ", working_hours=20)
#
# job_title_1.AssignJobClassification()
# job_title_1.AssignWorkingHours()
# job_title_2.AssignJobClassification()
# job_title_2.AssignWorkingHours()
