from sqlalchemy import create_engine, func, Column, Integer, String, Date, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.employe_position import employee_positions

class Employee(Base):
    __tablename__= "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    birth_date= Column(Date, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    salary = Column(Float(8,2), nullable=False)
    start_date= Column(DateTime, nullable=False, default=func.now())

    position = relationship("Position",secondary=employee_positions,back_populates="employees")
    company = relationship("Company", back_populates="employees")
    
    def __repr__(self):
        return f"Employee(id={self.id}, Position={self.position}, Name={self.name}, Surname={self.surname}, Birth_date={self.birth_date}, Salary={self.salary}, start_date={self.start_date})"
    

