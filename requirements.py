# zostavi list podmienok pre pre predlzenie zmluvy/skratenie zmluvy
from exceptions import AppExceptions


class RequirementsProlongedTenure:
    def __init__(self, id, prolonged_tenure: list) -> None:
        self.id = id
        self.prolonged_tenure = prolonged_tenure

    def __str__(self):
        return f"\nVyberte dôvod: \n{self.id}, {self.prolonged_tenure}"


class RequirementsShortenedTenure:
    def __init__(self, id, shortened_tenure: list):
        self.id = id
        self.shortened_tenure = shortened_tenure

    def __str__(self):
        return f"\n Vyberte dôvod: \n {self.id}, {self.shortened_tenure}"


class RequirementsList:
    def __init__(self):
        self.requirements_list = requirements_list

    def return_requirements_list(self):
        for rl in self.requirements_list:
            print(rl)


class Requirements:
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
