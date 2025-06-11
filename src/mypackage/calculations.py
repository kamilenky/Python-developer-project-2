# 4. calculations section
# tato cast vypocita sumu na vratenie zamestnavatelovi
# vyexportuje udaje v zhrnuti
# nie je dokoncena
# chcem pridat dalsie polozky do def print_summary
# chcem prepojit vstupy z employee_data, requirements
#calculations.py je zatial jedina cast, ktora sa nevola z start.py


from datetime import datetime, timedelta
import csv

from requests.packages import target

from api import get_exchange_rate


class RefundCalculator:
    def __init__(self, start_date: datetime, total_paid: float):
        self.start_date = start_date
        self.contract_duration = 3 * 365
        self.total_paid = total_paid
        self.end_date = self.start_date + timedelta(days=self.contract_duration)

    def calculate_refund(self):
        try:
            termination_date_input = input("Zadajte dátum ukončenia zmluvy (YYYY-MM-DD): ").strip()
            termination_date = datetime.strptime(termination_date_input, "%Y-%m-%d")

            if termination_date < self.start_date:
                print("Neplatný dátum ukončenia.")
                return

            if termination_date >= self.end_date:
                print(f"zmluva je platná len do {self.end_date}")
                return

            days_worked = (termination_date - self.start_date).days
            days_remaining_part = self.contract_duration - days_worked
            amount_day_net = self.total_paid / self.contract_duration
            refund_amount = amount_day_net * days_remaining_part

            rate = get_exchange_rate("EUR", "EUR")
            refund_currency = round(refund_amount * rate, 2) if rate else None

            self.print_summary(termination_date, days_worked, days_remaining_part, refund_amount, refund_currency)
            return refund_amount

        except ValueError:
            print("Neplatný formát dátumu.")
            return

    def print_summary(self, termination_date, days_worked, days_remaining_part, refund_amount, refund_currency):
        print("\nPredčasné ukončenie zmluvy - Zhrnutie")
        print(f"Začiatok zmluvy: {self.start_date.strftime('%d.%m.%Y')}")
        print(f"Plánovaný koniec zmluvy: {self.end_date.strftime('%d.%m.%Y')}")
        print(f"Skutočný dátum ukončenia: {termination_date.strftime('%d.%m.%Y')}")
        print(f"Vyplatená suma v hrubom: {self.total_paid:.2f} EUR")
        print(f"Odpracované dni: {days_worked}")
        print(f"Zostávajúce dni: {days_remaining_part}")
        print(f"Vrátená suma zamestnávateľovi: {refund_amount:.2f} EUR")
        print(f"Vrátená suma v zvolenej mene (EUR): {refund_currency:.2f}")

        with open("../summary.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "Začiatok zmluvy",
                "Plánovaný koniec zmluvy",
                "Skutočný dátum ukončenia",
                "Vyplatená suma",
                "Odpracované dni",
                "Zostávajúce dni",
                "Vrátená suma zamestnávateľovi"
            ])

            writer.writerow([
                self.start_date.strftime('%d.%m.%Y'),
                self.end_date.strftime('%d.%m.%Y'),
                termination_date.strftime('%d.%m.%Y'),
                f"{self.total_paid:.2f} EUR",
                days_worked,
                days_remaining_part,
                f"{refund_amount:.2f} EUR"
            ])

 # Employee's contract
start_date = datetime(2023, 1, 29)
total_paid = 2000  # EUR

# Create instance of calculator
calc = CalculateRefund(start_date, total_paid)

# Perform calculation
calc.calculate_refund()
