from sqlalchemy import func, Column, Integer, String, Date
from sqlalchemy.orm import relationship
from models.base import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    company_title = Column(String(255), nullable=False)
    company_code = Column(String(255), nullable=False, unique=True)
    industry = Column(String(255), nullable=False)
    founded_date = Column(Date, default=func.now())
    description = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    employees = relationship("Employee", back_populates="company")
    def __repr__(self):
        return f"Company(id = {self.id}.Company Name = {self.company_title}, industry = {self.industry}, Found_Date = {self.founded_date}, Description = {self.description}, Address = {self.address};)"

 