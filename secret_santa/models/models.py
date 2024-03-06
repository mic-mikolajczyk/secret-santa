import datetime
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    email: str
    password: str
    name: str | None = None
    events: list['Event'] = Field(default_factory=list)


class Gift(BaseModel):
    name: str = None
    description: str | None = None
    price: float | None = None


class Participant(BaseModel):
    name: str
    drawn_name: Optional['Participant'] = None
    whish_list: list[Gift] = Field(default_factory=list)


class Event(BaseModel):
    name: str
    event_id: str | None = None
    participants: list[Participant] = Field(default_factory=list)
    drawing_bucket: list[Participant] = Field(default_factory=list)
    date: datetime.datetime | None = None
    target_gift_price: float | None = None
