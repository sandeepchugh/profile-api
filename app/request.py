from uuid import UUID
from pydantic import BaseModel


class Request(BaseModel):
    path: str
    headers: dict
    path_parameters: dict
    http_method: str
    query_parameters: dict



class ProfileRequest(BaseModel):
    customer_id: UUID
