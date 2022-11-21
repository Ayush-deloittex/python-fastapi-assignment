from typing import List, Union, Optional

from pydantic import BaseModel


class MetricBase(BaseModel):
    title: str
    description: Union[str, None] = None


class MetricCreate(MetricBase):
    pass

class MetricUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class Metric(MetricBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    metrics: List[Metric] = []

    class Config:
        orm_mode = True
