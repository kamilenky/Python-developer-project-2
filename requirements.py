class Requirements:
    class RequirementsProlongedTenure:
        def __init__(self, id, prolonged_tenure: list) -> None:
            self.id = id
            self.prolonged_tenure = prolonged_tenure

        def __str__(self):
           return (f'n\"Vyberte dôvod: "
                    f"{self.id}, {self.prolonged_tenure}")

    class RequirementsShortenedTenure:
        def __init__(self, id, shortened_tenure: list ):
            self.id = id
            self.shortened_tenure = shortened_tenure



        def __str__(self):
            return (f"n\"Vyberte dôvod: "
                    f"{self.id},{self.shortened_tenure}")
            pass


        #zostavi list podmienok pre pre predlzenie zmluvy/skratenie zmluvy

    def list_requirements(self):
        for reason in self.reasons:
            reason.set_reason()
        pass


