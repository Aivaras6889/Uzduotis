from sqlalchemy import func, Column, Integer, String,  Date, DateTime, Float,ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.employe_position import employee_positions



class Position(Base):
    __tablename__= "positions"
    id = Column(Integer, primary_key=True)
    employees = relationship("Employee", secondary= employee_positions, back_populates="position")
    title = Column(String(255))
    description = Column(String(255),nullable=False)
    responsibilities = Column(String(255), nullable=False)
    requirements_id = Column(Integer, ForeignKey("position_requirements.id"), nullable=False)
    level_id= Column(Integer, ForeignKey("position_levels.id"), nullable=False)

    level = relationship("PositionLevel", back_populates="position")
    requirements = relationship("PositionRequirements", back_populates="position")
 

#Columns id , employees, title, description, responsibilities, requirements, level

    def __repr__(self):
        return f"Position(id = {self.id}. Employee_id = {self.employees} Title = {self.title}, Description = {self.description}, Responsibilities = {self.responsibilities}, Requirements = {self.requirements}, Level = {self.level} );"