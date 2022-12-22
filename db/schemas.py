from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class TicketBase(BaseModel):
    title: str
    description: str
    resolved_at: Optional[datetime]

class TicketCreate(TicketBase):
    created_at: datetime = datetime.now()
    pass

class Ticket(TicketBase):
    id: int
    created_at: datetime
    creator_id: int
    superuser: list[int] | None = None
    
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    tickets: list[int] = []
    profile: int|None

    class Config:
        orm_mode = True


class SuperuserBase(BaseModel):
    username: str


class SuperuserCreate(SuperuserBase):
    password: str


class Superuser(SuperuserBase):
    id: int
    is_active: bool
    tickets: list[int] = []

    class Config:
        orm_mode = True


class DepartmentBase(BaseModel):
    name: str
    address: str
    floor: int


class DepartmentCreate(DepartmentBase):
    pass


class Department(DepartmentBase):
    id: int
    profiles: list[int] = []

    class Config:
        orm_mode = True


class ProfileBase(BaseModel):
    surname: str
    name: str
    patronymic: str
    description: str
    user_id: int
    departments: list[int] = []


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: int

    class Config:
        orm_mode = True
