# zostavi list podmienok pre pre predlzenie zmluvy/skratenie zmluvy
from exceptions import AppExceptions




class RequirementsProlongedTenure:
    def __init__(self, id, prolonged_tenure) -> None:
        self.id = id
        self.prolonged_tenure = prolonged_tenure

    def __str__(self):
        return f"\nVyberte dôvod - bla bla: \n{self.id}, {self.prolonged_tenure}"


class RequirementsShortenedTenure:
    def __init__(self, id, shortened_tenure) -> None:
        self.id = id
        self.shortened_tenure = shortened_tenure

    def __str__(self):
        return f"\n Vyberte dôvod - ble ble: \n {self.id}, {self.shortened_tenure}"


class RequirementsList:
    def __init__(self, requirements_list):
        self.requirements_list = requirements_list


    def return_requirements_list(self):
        for rl in self.requirements_list:
            print(rl)

    def show_requirements(self):

        show_requirements = input("Zobraziť dôvody ukončenia zmluvy? (a/n): ").strip().lower()

        if show_requirements not in ["a", "n"]:
                raise AppExceptions.InvalidInputError("Zadajte iba 'a' alebo 'n'")

        if show_requirements == "a":
                self.return_requirements_list()
                return show_requirements
        else:
            print("ešte neviem, kam to presmerujem")
            exit()



class RequirementsById:
    def __init__(self):
        self.requirements = requirements

    def get_requirements_1_by_id(self):
        try:
            req_1_id = int(input("Vyberte podmienku pre...Zadajte číslo: ")).strip().lower()
            selected_req_1_id = next((r for r in self.reasons_1 if r.id == req_1_id), None)

            if selected_req_1_id:
                return RequirementsList.return_requirements_list()

            else:
                print('Neplatné číslo.')

        except AppExceptions.ValueError:
            print("Zadajte číslo zo zoznamu.")

reasons_1 = [
    RequirementsProlongedTenure(id=1, prolonged_tenure="ospravedlnená neprítomnosť zamestnanca"),
    RequirementsProlongedTenure(id=2, prolonged_tenure="výkon mimoriadnej služby")
]


reasons_2 = [
    RequirementsShortenedTenure(id=1, shortened_tenure="zamestnanec je preradený na inú pracovnú pozíciu"),
    RequirementsShortenedTenure(id=2, shortened_tenure="okamžité skončenie pracovného pomeru zamestnávateľom")
]

# requirements.py section
req_1 = RequirementsList(reasons_1)
req_2 = RequirementsList(reasons_2)
req_1.show_requirements()
req_2.show_requirements()
