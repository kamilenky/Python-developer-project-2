
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




