class Requirements:
    def __init__(self, reasons: list) -> None:
        self.reasons = reasons
        pass
        #zostavi list podmienok pre pre predlzenie zmluvy/skratenie zmluvy

    def list_requirements(self):
        for reason in self.reasons:
            reason.set_reason()
        pass


