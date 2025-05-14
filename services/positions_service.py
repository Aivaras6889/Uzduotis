import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import select
from models.position import Position
from models.employe_position import employee_positions
from database import getSession

#Columns id , employees, title, description, responsibilities, requirements, level
def displayPositions():
    try:
        session= getSession()
        stmt = select(Position)
        positions = session.execute(stmt).scalars().all()
        
        for position in positions:
            return f"{position.id}.{position.title}, {position.description}, {position.requirements}, {position.level}"
    
    except Exception as e:
        print(f"Error: {e}")

def add_positions():
    try:
        session = getSession()
        while True:
            position_title = input("Enter position title: ").strip()
            if position_title == 'q':
                break
            position_description =  input("Enter position description: ").strip()
            position_responsibilities = input("Enter position responsibilities: ").strip()
            position_requirements = input("Enter position requirements: ").strip()
            position_level = int(input("Enter level: "))
            position = Position(position_title = position_title, description = position_description, responsibilities=position_responsibilities, requirements= position_requirements, level=position_level)

            if session.query(Position).filter_by(title=position_title).first():
                print(f"Company '{position_title}' already exists. Please try again.")
                continue
            
            session.add(position)
        
        session.commit()
    except Exception as e:
            print(f"Error: {e}")

def update_companies():
    try:
        session = getSession()
        while True:
            positioniD_Entry= input("Enter position id: ")
            try:
                companyID= int(positioniD_Entry)
            except ValueError as e:
                print("Id must be number.")
                continue
            
            editposition = session.get(Position, companyID)
            if editposition:
                position_title = editposition.title
                print(f"Editing Position {position_title}:")
                print("Choice field you want to edit: ")
                print("_1.Title")
                print("_2.Description")
                print("_3.Responsibilities")
                print("_4.Requirements")
                print("_5.Level")
                
                #Columns id , employees, title, description, responsibilities, requirements, level
                preferred_column = int(input("Enter number of column which you want to edit:  "))
                try:
                    if not 1 <= preferred_column <= 8:
                        print("Invalid selection. Try again.")
                        continue
                except ValueError as e:
                    print("Error: enter a number between 1 and 8.")
                    continue
                if preferred_column == 1:
                    title = input("Enter new title of new position: ")
                    if title.strip():
                        editposition.title = title    
                        print("Successfully replaced title.")
                    else:
                        print("Position title cannot be empty.")
                        continue
                elif preferred_column == 2:
                    description = input("Enter position description: ")
                    if description.strip():
                        editposition.description=description
                        print("Successfully replaced description.")
                    else:
                        print("Position title cannot be empty.")
                        continue
                
                elif preferred_column == 3:
                    
                    responsibilities = input("Enter responsibilities of position: ")
                    if responsibilities.strip():
                        editposition.responsibilities=responsibilities
                        print("Successfully replaced responsibilities.")
                
                elif preferred_column == 4:
                    requirements = input("Enter Requirements: ")
                    if requirements.strip():
                        editposition.requirements=requirements
                        print("Successfully added new description.")
                elif preferred_column == 5:
                    try: 
                        level_entry = input("Enter level: ")
                        level= int(level_entry)
                    except ValueError as e:
                        print(f"Error: {e}")

                    if level.strip():
                        editposition.level=level
                        print("Successfully replaced level.")

                session.commit()
                
                continue_update = input("\nDo you want to update another field for this Position? (y/n): ")
                
                if continue_update.lower() != 'y':
                    break              
                   
    except Exception as e:
        print(f"Error: {e}")

def delete_companies():
    try:
        session = getSession()
        while True:
            preferred_ID = input("Enter position id you want to delete: ")

            try:
                position_id = int(preferred_ID)
            except ValueError as e:
                print(f"Id must be a number. {e}")
                continue

            positiontodelete = session.get(Position, position_id)

            if positiontodelete:
                position_title=positiontodelete.title
                confirm = input("Enter 'y'- (yes) or 'n' - (no):  ")
                if confirm.lower() != 'y':
                     print("Deletion canceled.")
                     continue
                
                session.delete(positiontodelete)
                session.commit()
                
                print(f"Successfully deleted {position_title} position.")
                
                another = input("Delete another position? (y/n): ")
                if another.lower() != 'y':
                    break
            else:
                print(f"Company with ID: {position_title} not found")



    except Exception as e:
        print(f"Error: {e}")