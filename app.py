from database import createDataBase
from views.menu_view import Menu

# "Importuoti duomenu bazes funkcija" ir "Display Menu"

try:    
    createDataBase()
    Menu()
except Exception as e: 
    print(f"Error: {e}")
