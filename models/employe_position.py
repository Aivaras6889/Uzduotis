
from sqlalchemy import Column, ForeignKey, Integer, Table
from models.base import Base

employee_positions= Table(
    "employee_positions",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id"), primary_key= True),
    Column("position_id", Integer, ForeignKey("positions.id"), primary_key= True),
)