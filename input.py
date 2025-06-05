def show_data(self):
    show_employees = input("Zobraziť zoznam zamestnancov (a/n): ").strip().lower()

def calculate_refund(self):
    try:
        termination_date_input = input("Zadajte dátum ukončenia zmluvy (YYYY-MM-DD): ").strip()
        termination_date = datetime.strptime(termination_date_input, "%Y-%m-%d")

def show_requirements(self, prompt_text="\nZobraziť dôvody na predĺženie/skrátenie zmluvy? (a/n): "):
    show_requirements = input(prompt_text).strip().lower()

def get_requirements_by_id(self, prompt_text="\nVyberte podmienku. Zadajte číslo: "):
    try:
        req_id = int(input(prompt_text))
        selected_req_id = next((r for r in self.requirements_list if r.id == req_id), None)

def get_employee_by_id(self):
    try:
        emp_id = int(input("Zadajte ID zamestnanca. Zadajte číslo: ").strip().lower())
        selected_emp = next((e for e in self.employee_data if  e.id == emp_id), None)