
from src.mypackage.employee import EmployeeManager

#option 1
# import sys
#
# sys.path.append("src")
#
# from mypackage import employee
#
# employee.greet()


# option 2
import src.mypackage.employee

def main ():
    print("start")
    src.mypackage.employee.greet()

    # shows employees list
    employee_manager = EmployeeManager()
    try:
        employee_manager.show_employees()
    except exception as e:
        print(f"Chyba: {e}")

    # shows emloyee by id
    try:
        employee_manager.show_employee_by_id()
    except exception as e:
        print(f"Chyba: {e}")

if __name__ == '__main__':
    main()


employee_data = [
    EmployeeData(id=1, name="Adam", surname="A", job_classification="Opatrovateľ",
                 contribution_amount_gross=2000,
                 contribution_amount_net=round(2000 * 0.81,2), start_date=datetime(2025, 1, 1)),
    EmployeeData(id=2, name="Braňo", surname="B", job_classification="Sociálny pracovník",
                 contribution_amount_gross=1500,
                 contribution_amount_net=round(1500 * 0.81,2), start_date=datetime(2025, 1, 1)),
    EmployeeData(id=3, name="Cyril", surname="C", job_classification="Inštruktor sociálnej rehabilitácie",
                 contribution_amount_gross=2000,
                 contribution_amount_net=round(2000 * 0.81,2), start_date=datetime(2025, 1, 1))
]

