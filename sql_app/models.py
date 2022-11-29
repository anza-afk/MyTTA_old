
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base


superuser_ticket = Table(
    "superuser_ticket",
    Base.metadata,
    Column("superuser_id", ForeignKey("superusers.id"), primary_key=True),
    Column("troubleticket_id", ForeignKey("troubletickets.id"), primary_key=True),
)

profile_department = Table(
    "profile_department",
    Base.metadata,
    Column("profile_id", ForeignKey("profiles.id"), primary_key=True),
    Column("department_id", ForeignKey("departments.id"), primary_key=True),
)

class TroubleTicket(Base):
    __tablename__ = "troubletickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    creator_id = Column(Integer, ForeignKey("users.id"))
    worker_id = relationship("Superuser", secondary=superuser_ticket, back_populates="troubletickets")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    profile = relationship("Profile", back_populates="user", uselist=False)
    tickets = relationship("Troubleticket")


class Superuser(Base):
    __tablename__ = "superusers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    username = Column(String, index=True)

    troubleticket = relationship("Troubleticket", secondary=superuser_ticket, back_populates="superusers")


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    surname = Column(String, index=True)
    name = Column(String, index=True)
    patronymic = Column(String, index=True)

    department = relationship('Department', secondary=profile_department, back_populates='profiles')
    user = relationship("User", back_populates="profile")


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String)
    floor =  Column(Integer)

    department = relationship('Profile', secondary=profile_department, back_populates='departments')