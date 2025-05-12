class JobTenureProlonged:
    def __init__(self, prolonged_tenure: str, days: int) -> None:
        self.prolonged_tenure = prolonged_tenure
        self.days = days
        # zvaliduje podmienku pre predlzenie zmluvy

    def set_reason(self) -> None:
        print(f"Dovod nepritomnosti je {self.prolonged_tenure}")