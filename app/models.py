from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

class Mentor(Base):
    __tablename__ = "mentors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    skills = Column(String)
    active = Column(Boolean, default=True)
    experience_of_years = Column(Integer, nullable=True)
    linkedin_url = Column(String, nullable=True)
    github_url = Column(String, nullable=True)
    instagram_url = Column(String, nullable=True)
    photo_url = Column(String, nullable=True)
    location = Column(String, index=True, nullable=True)