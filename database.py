from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.employee import Employee
from models.position import Position 
from models.company import Company



# == Importuoti lenteles ...

engine = create_engine("mysql://root:Pqj]a,(2g}pysMK@localhost:3306/paskaitasqlalch")


def createDataBase():
    Base.metadata.create_all(engine)

def getSession():
    Session = sessionmaker(bind=engine)
    return Session()