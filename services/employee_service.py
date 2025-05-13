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
            
            print("Choice: ")
            print("_1 to add new employee;")
            print("_2 to add new company;")
            print("_3 to add new position;")
            print("_4 to return back;")
            choice = int(input("Enter(1/4)"))
            
            if choice == 1:
                name = input("Enter employee name: ")
                surname = input("Enter employee surname: ")
                birth_date= input("Enter birth date(xxxx/xx/xx): ")
                salary = float(input("Enter employee Salary(x...x.xx): "))
                company_id = int(input("Enter company ID: "))
                company = session.get(Company, company_id)
                if not company:
                    print("Invalid company ID. Please try again.")
                    continue

                employee = Employee(name=name, surname=surname, birth_date=birth_date, salary=salary, company_id =company_id)
                session.add(employee)
                print(f"Successfully added: {name}")
            if choice == 2:
                 company_name = input("Enter company title: ")
                 company_code = ''.join(random.choices(string.digits + string.ascii_uppercase, k=9))
                 industry = input("Enter Industry title: ")
                 description = input("Enter Company description:")
                 address = input("Enter Company Address: ")
                 company = Company(company_name=company_name, company_code=company_code, industry=industry, description= description, address = address )
                 session.add(company)
            if choice == 3:
                pos_title = input("Enter position title: ")
                position_desc = input("Enter position description: ")
                pos_responsibilities = input("Enter position responsibilities: ")
                pos_requirements = input("Enter position requirements: ")
                pos_level = int(input("Enter level: "))
                position = Position(title=pos_title, description=position_desc, responsibilities=pos_responsibilities, requirements=pos_requirements, level = pos_level)
                session.add(position)
            if choice == 4:
                break
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
                print("5. Company ID")
                print("6. Start date")
                print("7. Assign position")
                print("8. Return")
                
              
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
                        
                elif selected_column == 5:
                    try:
                        company_id_input = input("Enter new company ID: ")
                        company_id = int(company_id_input)
                        company = session.get(Company, company_id)
                        if company:
                            selected_employee.company_id = company_id
                            print(f"Employee assigned to new company: {company.company_name}")
                        else:
                            print("Company with this ID not found.")
                            continue
                    except ValueError:
                        print("Invalid company ID format. Enter a number.")
                        continue
                        
                elif selected_column == 6:
                    try:
                        start_date = input("Enter new start date (yyyy-mm-dd): ")
                        parsed_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
                        selected_employee.start_date = parsed_date
                        print("Start date successfully updated.")
                    except ValueError:
                        print("Invalid date format. Use yyyy-mm-dd format.")
                        continue
                        
                elif selected_column == 7:
                    try:
                        position_id_input = input("Enter position ID: ")
                        position_id = int(position_id_input)
                        position = session.get(Position, position_id)
                        if position:
                            # Check if employee already has this position
                            has_position = False
                            for pos in selected_employee.positions:
                                if pos.position_id == position_id:
                                    has_position = True
                                    break
                            
                            if has_position:
                                print(f"Employee already has this position: {position.title}")
                            else:
                                selected_employee.positions.append(position)
                                print(f"Position '{position.title}' successfully assigned to employee.")
                        else:
                            print("Position with this ID not found.")
                            continue
                    except ValueError:
                        print("Invalid position ID format. Enter a number.")
                        continue
                        
                elif selected_column == 8:
                    print("Returning to employee list...")
                    break
                
            
                session.commit()
                
                
                continue_update = input("\nDo you want to update another field for this employee? (y/n): ")
                if continue_update.lower() != 'y':
                    break
        except Exception as e:
            print(f"Error: {e}")

# update_employees()

def delete_user_data():
    displayEmployees()
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