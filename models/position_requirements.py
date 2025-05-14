from sqlalchemy import func, Column, Integer, String, Date
from sqlalchemy.orm import relationship
from models.base import Base


class PositionRequirements(Base):
    __tablename__ = "position_requirements"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    position = relationship("Position", back_populates="requirements")
    

    def __repr__(self):
        return f"ID= {self.id}, Title={self.title}, Description={self.description}" 