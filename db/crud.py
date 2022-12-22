from sqlalchemy.orm import Session
from passlib.context import CryptContext

from . import models, schemas


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    password_hash = Hasher.get_password_hash(user.password)
    db_user = models.User(
        email = user.email,
        hashed_password = password_hash
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_superuser(db: Session, superuser_id: int):
    return db.query(models.Superuser).filter(models.Superuser.id == superuser_id).first()


def get_superuser_by_username(db: Session, username: str):
    return db.query(models.Superuser).filter(models.Superuser.username == username).first()


def get_superusers(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.Superuser).offset(offset).limit(limit).all()


def create_superuser(db: Session, superuser: schemas.UserCreate):
    password_hash = Hasher.get_password_hash(superuser.password)
    db_superuser = models.Superuser(
        email = superuser.email,
        hashed_password = password_hash
    )
    db.add(db_superuser)
    db.commit()
    db.refresh(db_superuser)
    return db_superuser


def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()


def get_tickets(db:Session, offset: int = 0, limit: int = 100):
    return db.query(models.Ticket).offset(offset).limit(limit).all()


def create_ticket(db:Session, ticket: schemas.TicketCreate, user_id: int):
    user_id = 0
    db_ticket = models.Ticket(
        **ticket.dict(),
        creator_id=user_id
        )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.profile.id == profile_id).first()


def get_profiles(db:Session, offset: int = 0, limit: int = 100):
    return db.query(models.Profile).offset(offset).limit(limit).all()


def create_profile(db:Session, profile: schemas.ProfileCreate, owner_id: int):
    db_profile = models.Profile(
        **profile.dict(),
        user_id = owner_id
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def get_department(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id == department_id).first()


def get_departments(db:Session, offset: int = 0, limit: int = 100):
    return db.query(models.Department).offset(offset).limit(limit).all()


def create_department(db:Session, department: schemas.DepartmentCreate):
    db_department = models.Department(
        **department.dict(),
    )
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department