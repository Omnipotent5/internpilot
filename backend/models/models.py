from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    website = Column(String, index=True)
    hiring_page = Column(String, index=True)
    job_listings = Column(String, index=True)

class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    required_skills = Column(String, index=True)
    preferred_skills = Column(String, index=True)
    technologies = Column(String, index=True)
    responsibilities = Column(String, index=True)

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    job_description_id = Column(Integer, ForeignKey("job_descriptions.id"))

    user = relationship("User", back_populates="applications")
    company = relationship("Company", back_populates="applications")
    job_description = relationship("JobDescription", back_populates="applications")

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String, index=True)

    user = relationship("User", back_populates="resumes")

class CoverLetter(Base):
    __tablename__ = "cover_letters"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String, index=True)

    user = relationship("User", back_populates="cover_letters")

class EmailDraft(Base):
    __tablename__ = "email_drafts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    subject = Column(String, index=True)
    content = Column(String, index=True)

    user = relationship("User", back_populates="email_drafts")
