import json
from pydantic import BaseModel, ValidationError, validator
from aiohttp import web
from typing import Optional

def raise_http_error(error_class, list_of_errors):
    raise error_class(
        text=json.dumps(
            {
                'status': 'validation error',
                'descriptions': [error['msg'] for error in list_of_errors]
            }
        ),
        content_type="application/json",
    )

def validate(data, validation_class):
    try:
        return validation_class(**data).dict(exclude_none=True)
    except ValidationError as err:
        raise_http_error(web.HTTPInternalServerError, err.errors())


class AdvPostModel(BaseModel):
    header: str
    description: str
    owner: str

    @validator('header')
    def check_header(cls, value):
        if len(value) > 42:
            raise ValueError('header is too long (must be less than 42 chars)')
        elif len(value) == 0:
            raise ValueError('header field shoulnd not be empty')
        return value

    @validator('description')
    def check_description(cls, value):
        if len(value) > 1000:
            raise ValueError('description is too long (must be less than 1000 chars)')
        elif len(value) == 0:
            raise ValueError('description field shoulnd not be empty')
        return value

    @validator('owner')
    def check_owner(cls, value):
        if len(value) > 32:
            raise ValueError('owner name is too long (must be less than 32 chars)')
        elif len(value) == 0:
            raise ValueError('owner field shoulnd not be empty')
        return value


class AdvPatchModel(BaseModel):
    header: Optional[str]
    description: Optional[str]
    owner: Optional[str]

    @validator('header')
    def check_header(cls, value):
        if len(value) > 42:
            raise ValueError('header is too long (must be less than 42 chars)')
        elif len(value) == 0:
            raise ValueError('header field shoulnd not be empty')
        return value

    @validator('description')
    def check_description(cls, value):
        if len(value) > 1000:
            raise ValueError('description is too long (must be less than 1000 chars)')
        elif len(value) == 0:
            raise ValueError('description field shoulnd not be empty')
        return value

    @validator('owner')
    def check_owner(cls, value):
        if len(value) > 32:
            raise ValueError('owner name is too long (must be less than 32 chars)')
        elif len(value) == 0:
            raise ValueError('owner field shoulnd not be empty')
        return value
