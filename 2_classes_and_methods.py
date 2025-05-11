# employee data

class EmployeeData:
    def ReturnEmployeeDataClass(self):
        pass


class EmployeeName:
    def ReturnEmployeeName(self):
        pass


class JobClassification:
    def __init__(self, job_classification: str, working_hours: int) -> None:
        self.job_classificaiton = job_classification
        self.working_hours = working_hours
        # priradi pracovne zaradenie zamestnancovi

    def AssignJobClassification(self) -> None:
        print(f"Pracovné zaradenienie: {self.job_classificaiton}")

    def AssignWorkingHours(self) -> None:
        print(f"Pracovný uväzok: {self.working_hours}")

    def assign_contribution_rate(self):
        full_contribution = 100
        if job_classification=="Sociálny pracovník":
            return full_contribution*1
        elif job_classification=="Opatrovateľ":
            return full_contribution*0.5




job_title_1 = JobClassification(job_classification="Sociálny pracovník", working_hours=40)
job_title_2 = JobClassification(job_classification="Opatrovateľ", working_hours=20)

job_title_1.AssignJobClassification()
job_title_1.AssignWorkingHours()
job_title_2.AssignJobClassification()
job_title_2.AssignWorkingHours()








class EmployementType:
    def AssignEmployementType(self):
        print("Part-time")


class ContributionAmount:
    def SetFull(self):
        pass

    def SetReduced(self):
        pass



# amendement requirements
class Requirements:
    def __init__(self, reasons: list) -> None:
        self.reasons = reasons
        #zostavi list podmienok pre pre predlzenie zmluvy/skratenie zmluvy



class JobTenureProlonged:
    def __init__(self, prolonged_tenure: str, days: int) -> None:
        self.prolonged_tenure = prolonged_tenure
        self.days = days
        # zvaliduje podmienku pre predlzenie zmluvy

class JobTenureShortened:
    def __init__(self, shortened_tenure:str, days: int) -> None:
        self.shortened_tenure = shortened_tenure
        self.days = days

        # zvaliduje podmienku pre predlzenie zmluvy


reasons = [
    JobTenureProlonged(prolonged_tenure="ospravedlnená neprítomnosť zamestnanca", days=5),
    JobTenureProlonged(prolonged_tenure="neospravedlnená neprítomnosť zamestnanca", days=1),
    JobTenureProlonged(prolonged_tenure="výkon mimoriadnej služby", days=1),
    JobTenureProlonged(prolonged_tenure="výkon väzby alebo nepodmienečného trestu odňatia slobody", days=0),
    JobTenureShortened(shortened_tenure="zamestnanec je preradený na inú pracovnú pozíciu", days=30)
]

requirements = Requirements(reasons=reasons)
print(requirements)



class JobTenureDays:
    pass


class EmployeeSideObstacles:
    pass


# other

class ContractDates:
    pass


class CalculateJobTenurePeriod:
    pass


class CalculateContributionAmount:
    pass
