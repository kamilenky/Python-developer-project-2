from datetime import datetime, timedelta

base = 1096
contract_duration = 3*365
remaining_part = base - contract_duration


contribution_amount_net = 1215
amount_day_net = contribution_amount_net/contract_duration
refund_amount = remaining_part*amount_day_net


class CalculateRefund:
    def __init__(self):
        self.start_date = datetime(2025, 1, 1)
        self.end_date = self.start_date + timedelta(days=self.contract_duration)
        self.contract_duration = 3*365
        self.refund_amount = refund_amount

    def calculate_refund(self):
        try:
            end_date_input = input("Zadajte dátum ukončenia zmluvy: ").strip()
            end_date = datime.strptime(end_date_input, "%d-%m-%y")





