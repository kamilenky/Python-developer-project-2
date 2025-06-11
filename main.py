#option 2
import sys

sys.path.append("src")

from mypackage import employee

employee.greet()


# option 2
import src.mypackage.employee

def main ():
    print("start")
    src.mypackage.employee.greet()

if __name__ == '__main__':
    main()


