import sys
import os
import datetime as dt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.employee import Employee
from models.company import Company
from models.position import Position
from sqlalchemy import select
from database import getSession 
import random
import string



def displayEmployees():
    session= getSession()
    stmt = select(Employee)
    employees = session.execute(stmt).scalars().all()
    
    for employee in employees:
        print(f"{employee.id}.{employee.name}, {employee.surname}, {employee.birth_date}, {employee.salary:.2f}, {employee.company_id}, {employee.start_date}".format(employee.salary,2))
    
    return employee.id, employee.position, employee.name, employee.surname, employee.birth_date, employee.salary,employee.company_id, employee.start_date




# Darbuotojo_pridejimas
def employee_insert():
    try:
        session = getSession()
        while True:
            name = input("Enter employee name: ")
            if name == "q":
                break
            surname = input("Enter employee surname: ")
            try:
                birth_date= input("Enter birth date(xxxx/xx/xx): ")
                parsed_birth_date = dt.datetime.strptime(birth_date, "%Y-%m-%d")
            except ValueError as e:
                print(f"Error: {e}")
                continue
            salary = float(input("Enter employee Salary(x...x.xx): "))
            company_id = int(input("Enter company ID: "))
            company = session.get(Company, company_id)
            
            if not company:
                print("Invalid company ID. Please try again.")
                continue

            employee = Employee(name=name, surname=surname, birth_date=parsed_birth_date, salary=salary, company_id =company_id)
            session.add(employee)
            print(f"Successfully added: {name}")            
        session.commit()
    except Exception as e:
        print(f"Ivyko klada {e}")

def asign_company_position_to_employe(): 
    session = getSession()
    while True:
        print("Choice: ")
        print("_1 to assign a company to an employee;")
        print("_2 to assign a position to an employee;")
        print("_3 to return back;")
        choice = int(input("Enter(1/3): "))

        if choice == 1: 
            employee_id = int(input("Enter employee ID: "))
            company_id = int(input("Enter company ID: "))

            employee = session.get(Employee, employee_id)
            company = session.get(Company, company_id)

            if employee and company:
                employee.company_id = company_id
                session.commit()

                print(f"Successfully assigned company '{company.company_name}' to employee '{employee.name}'.")
            else:
                print("Invalid employee or company ID.")
        if choice == 2:
            employee_id = int(input("Enter employee ID: "))
            position_id = int(input("Enter position ID: "))

            employee = session.get(Employee, employee_id)
            position = session.get(Position, position_id)

            if employee and position: 
                employee.position.append(position)
                session.commit()
                print(f"Successfully assigned position '{position.title}' to employee '{employee.name}'.")
            else:
                print("Invalid employee or position ID.")

        elif choice == 3:
            break

# asign_company_to_employe()

def update_employees():
        try:
            displayEmployees()
            session = getSession()
            
            while True:
                
                select_id_input = input("Select employee ID to edit (or press Enter to return): ")
                
                
                if select_id_input == "":
                    print("Returning to main menu...")
                    break
                
                
                try:
                    select_id = int(select_id_input)
                except ValueError:
                    print("Error: ID must be a number. Try again.")
                    continue
                
     
                selected_employee = session.get(Employee, select_id)
                
               
                if not selected_employee:
                    print(f"Employee with ID {select_id} not found. Try again.")
                    continue
                    
               
                print(f"\nEditing employee: {selected_employee.name} {selected_employee.surname}")
                print("-----------------------------")
                
                
                print("1. Name")
                print("2. Surname")
                print("3. Birth date")
                print("4. Salary")
                print("5. Start date")
                
              
                try:
                    selected_column = int(input("Select what to change (1-8): "))
                    if not 1 <= selected_column <= 8:
                        print("Invalid selection. Try again.")
                        continue
                except ValueError:
                    print("Error: enter a number between 1 and 8.")
                    continue
                
                
                if selected_column == 1:
                    new_name = input("Enter new name: ")
                    if new_name.strip():  
                        selected_employee.name = new_name
                        print("Name successfully updated.")
                    else:
                        print("Name cannot be empty.")
                        continue
                        
                elif selected_column == 2:
                    new_surname = input("Enter new surname: ")
                    if new_surname.strip():
                        selected_employee.surname = new_surname
                        print("Surname successfully updated.")
                    else:
                        print("Surname cannot be empty.")
                        continue
                        
                elif selected_column == 3:
                    try:
                        birth_date = input("Enter new birth date (yyyy-mm-dd): ")
                        parsed_date = dt.datetime.strptime(birth_date, "%Y-%m-%d").date()
                        selected_employee.birth_date = parsed_date
                        print("Birth date successfully updated.")
                    except ValueError:
                        print("Invalid date format. Use yyyy-mm-dd format.")
                        continue
                        
                elif selected_column == 4:
                    try:
                        salary_input = input("Enter new salary: ")
                        salary = float(salary_input)
                        if salary < 0:
                            print("Salary cannot be negative.")
                            continue
                        selected_employee.salary = salary
                        print("Salary successfully updated.")
                    except ValueError:
                        print("Invalid salary format. Enter a number.")
                        continue
                # Iskelti darbuotojo darbovietes antaujinima per kompanijos service faila dar neigivendinta
                # Taip pat su pozicija atnaujinti per pozicijos service faila dar neigyvendinta 

                elif selected_column == 5:
                    try:
                        start_date = input("Enter new start date (yyyy-mm-dd): ")
                        parsed_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
                        selected_employee.start_date = parsed_date
                        print("Start date successfully updated.")
                    except ValueError:
                        print("Invalid date format. Use yyyy-mm-dd format.")
                        continue
            
                session.commit()
                
                
                continue_update = input("\nDo you want to update another field for this employee? (y/n): ")
                if continue_update.lower() != 'y':
                    break
        except Exception as e:
            print(f"Error: {e}")

# update_employees()

def delete_user_data():
    session = getSession()
    try:
        while True:
            
                employee_id_input = input("Enter the ID of the employee to delete (or press Enter to exit): ")
                
                if employee_id_input == "":
                    print("Returning to main menu...")
                    break
                
                try:
                    employee_id = int(employee_id_input)
                except ValueError:
                    print("Error: ID must be a number")
                    continue
                
                employee_to_delete = session.get(Employee, employee_id)
                
                if employee_to_delete:
                    employee_name = employee_to_delete.name
                    
                    confirm = input(f"Are you sure you want to delete {employee_name}? (y/n): ")
                    if confirm.lower() != 'y':
                        print("Deletion cancelled.")
                        continue
                        
                    session.delete(employee_to_delete)
                    session.commit()
                    
                    print(f"Successfully deleted employee: {employee_name}")
                    
                    another = input("Delete another employee? (y/n): ")
                    if another.lower() != 'y':
                        break
                else:
                    print(f"Employee with ID {employee_id} not found")
            
    except Exception as e:
        print(f"Error: {e}")