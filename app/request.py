from uuid import UUID
from pydantic import BaseModel, Field


class Request(BaseModel):
    path: str
    headers: dict
    path_parameters: dict = Field({}, alias="pathParameters")
    http_method: str = Field('', alias="httpMethod")
    query_parameters: dict = Field({}, alias="queryStringParameters")

    class Config:
        allow_population_by_field_name = True


class ProfileRequest(BaseModel):
    customer_id: str = Field('', alias="customerId")

    class Config:
        allow_population_by_field_name = True


def create(event):
    request = Request(**event)
    return ProfileRequest(**request.query_parameters)