import os 
import random
import string
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.company import Company
from sqlalchemy import select

from datetime import date
from database import getSession


def displayCompanies():
    try:
        session= getSession()
        stmt = select(Company)
        companies = session.execute(stmt).scalars().all()
        
        for company in companies:
            return f"{company.id}.{company.company_title}, {company.company_code}, {company.industry}, {company.founded_date}, {company.description}, {company.address}"
            # return company.id, company.company_title, company.company_code, company.industry, company.founded_date, company.description, company.address
    except Exception as e:
        print(f"Error: {e}")
## columns: vid, vcompany_name, vcompany_code, vindustry, vfounded_date, vdescriptions , vaddress

def add_companies():
    try:
        session = getSession()
        while True:
            company_name = input("Enter company title: ")
            if company_name == 'q':
                break
            company_code = ''.join(random.choices(string.digits + string.ascii_uppercase, k=9))
            industry = input("Enter Industry title: ")
            description = input("Enter Company description:")
            address = input("Enter Company Address: ")
            company = Company(company_name=company_name, company_code=company_code, industry=industry, description= 
            description, address = address )
        
            if session.query(Company).filter_by(company_name=company_name).first():
                print(f"Company '{company_name}' already exists. Please try again.")
                continue
            
            session.add(company)
        
        session.commit()
    except Exception as e:
            print(f"Error: {e}")

def update_companies():
    try:
        session = getSession()
        while True:
            companyiD_Entry= input("Enter company id: ")
            try:
                companyID= int(companyiD_Entry)
            except ValueError as e:
                print("Id must be number.")
                continue
            
            editcompany = session.get(Company, companyID)
            if editcompany:
                company_title = editcompany.company_title
                print(f"Editing Company {company_title}:")
                print("Choice field you want to edit: ")
                print("_1.Company Title")
                print("_2.Company Code")
                print("_3.Industry")
                print("_4.Description")
                print("_5.Address")
                

                preferred_column = int(input("Enter number of column which you want to edit:  "))
                try:
                    if not 1 <= preferred_column <= 8:
                        print("Invalid selection. Try again.")
                        continue
                except ValueError as e:
                    print("Error: enter a number between 1 and 8.")
                    continue
                if preferred_column == 1:
                    company_title = input("Enter new title of company: ")
                    if company_title.strip():
                        editcompany.company_title = company_title    
                        print("Successfully changed company title.")
                    else:
                        print("Company title cannot be empty.")
                        continue
                elif preferred_column == 2:
                    company_code = input("Enter company code: ")
                    if company_code.strip():
                        editcompany.company_code=company_code
                        print("Successfully changed company code.")
                
                elif preferred_column == 3:
                    industry = input("Enter industry of company: ")
                    if industry.strip():
                        editcompany.industry=industry
                        print("Successfully added new industry.")
                elif preferred_column == 4:
                    description = input("Enter description: ")
                    if description.strip():
                        editcompany.description=description
                        print("Successfully added new description.")
                elif preferred_column == 5:
                    address = input("Enter address: ")
                    if address.strip():
                        editcompany.address=address
                        print("Successfully added new address.")
                session.commit()
                
                continue_update = input("\nDo you want to update another field for this Company? (y/n): ")
                
                if continue_update.lower() != 'y':
                    break              
                   
    except Exception as e:
        print(f"Error: {e}")

def delete_companies():
    try:
        session = getSession()
        while True:
            preferred_ID = input("Enter company id you want to delete: ")

            try:
                company_id = int(preferred_ID)
            except ValueError as e:
                print(f"Id must be a number. {e}")
                continue

            companytodelete = session.get(Company, company_id)

            if companytodelete:
                company_title=companytodelete.company_title

                confirm = input("Enter 'y'- (yes) or 'n' - (no):  ")
                if confirm.lower() != 'y':
                     print("Deletion canceled.")
                     continue
                session.delete(companytodelete)
                session.commit()
                
                print(f"Successfully deleted company: {company_title}")
                
                another = input("Delete another company? (y/n): ")
                if another.lower() != 'y':
                    break
            else:
                print(f"Company with ID: {company_id} not found")



    except Exception as e:
        print(f"Error: {e}")