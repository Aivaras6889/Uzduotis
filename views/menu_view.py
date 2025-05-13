import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services.employee_service import *


# Session = sessionmaker(bind=engine)
# with Session() as session:
def Menu():
    while True:
        print("===\tMenu:\t===\n")
        print("_1. Display Employees.")
        print("_2. Add Employee.")
        print("_3. Assign Employee to company or position")
        print("_4. Update Employee")
        print("_5. Delete_Employee")
        print("_10. Exit")
        pasirinkimas = int(input("Iveskite pasirinikima(1/10):"))

        match pasirinkimas:
            case 1:
                displayEmployees()
            case 2: 
                employee_insert()
            case 3: 
                asign_company_position_to_employe()
            case 4: 
                update_employees()
            case 5:
                delete_user_data()
            case 10: 
                print("Iki ... :)")
                break
            case _:
                print("Netinkamas pasirinkimas ...")
                continue

