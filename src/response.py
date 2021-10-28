import uuid
from typing import List
from uuid import UUID
from pydantic import BaseModel, Field


class Preference(BaseModel):
    value: str
    category: str


class Profile(BaseModel):
    customer_id: UUID = Field(default_factory=uuid.uuid4)
    first_name: str
    last_name: str
    preferences: List[Preference] = Field(default_factory=list)


