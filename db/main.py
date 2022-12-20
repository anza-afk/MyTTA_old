from typing import Generator
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

db_router = APIRouter()


@db_router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@db_router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@db_router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@db_router.post("/users/{user_id}/profile/", response_model=schemas.Profile)
def create_profile_for_user(
    user_id: int,
    profile: schemas.ProfileCreate,
    db: Session = Depends(get_db)
    ):
    return crud.create_profile(
        db,
        profile=profile,
        owner_id=user_id
        )


@db_router.post("/users/{user_id}/tickets/", response_model=schemas.Ticket)
def create_ticket_for_user(
    user_id: int,
    ticket: schemas.TicketCreate,
    db: Session = Depends(get_db)
):
    return crud.create_ticket(db=db, ticket=ticket, user_id=user_id)


@db_router.get("/tickets/", response_model=list[schemas.Ticket])
def read_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tickets = crud.get_tickets(db, skip=skip, limit=limit)
    return tickets