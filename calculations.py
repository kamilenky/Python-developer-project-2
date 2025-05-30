from datetime import datetime, timedelta




base = 1096
contract_duration = 3*365
remaining_part = base - contract_duration


contribution_amount_net = 1215
amount_day_net = contribution_amount_net/contract_duration
refund_amount = remaining_part*amount_day_net


class CalculateRefund:
    def __init__(self):
        pass

