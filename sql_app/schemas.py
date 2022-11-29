from pydantic import BaseModel


class TroubleTIcketBase(BaseModel):
    title: str
    description: str
    worker_id: int | None = None

class TroubleTIcketCreate(TroubleTIcketBase):
    pass


class TroubleTIcket(TroubleTIcketBase):
    id: int
    creator_id: int

    class Config:
        orm_mode = True
