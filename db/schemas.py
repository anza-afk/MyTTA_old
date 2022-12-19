from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    description: str
    worker_id: int | None = None
    creator_id: int

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    tickets: list[int] = []
    profile: int

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
