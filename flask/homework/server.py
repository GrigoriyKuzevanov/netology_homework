import pydantic
from flask import (
    Flask,
    jsonify,
    request,
)
from flask.views import MethodView
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    create_engine,
    func,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Type, Optional
from sqlalchemy.exc import IntegrityError


app = Flask('app')


class HttpError(Exception):

    def __init__(self, status_code: int, message: str | dict | list):
        self.status_code = status_code
        self.message = message


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify({
        'status': 'error',
        'message': error.message
    })
    response.status_code = error.status_code
    return response


DSN = 'postgresql://test:1490@127.0.0.1:5431/test_db'


engine = create_engine(DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class AdModel(Base):

    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True)
    header = Column(String(42), nullable=False, unique=True)
    description = Column(String(400), nullable=False)
    creation_date = Column(DateTime, server_default=func.now())
    owner = Column(String(32), nullable=False)


Base.metadata.create_all(engine)


class CreateAdSchema(pydantic.BaseModel):
    header: str
    description: str
    owner: str

    @pydantic.validator('header')
    def check_header(cls, value: str):
        if len(value) > 42:
            raise ValueError('header must be less than 42 chars')
        return value

    @pydantic.validator('description')
    def check_description(cls, value: str):
        if len(value) > 400:
            raise ValueError('description must be less than 400 chars')
        return value

    @pydantic.validator('owner')
    def check_owner(cls, value: str):
        if len(value) > 32:
            raise ValueError('owner_name must be less than 42 chars')
        return value


class PatchAdSchema(pydantic.BaseModel):
    header: Optional[str]
    description: Optional[str]
    owner: Optional[str]

    @pydantic.validator('header')
    def check_header(cls, value: str):
        if len(value) > 42:
            raise ValueError('header must be less than 42 chars')
        return value

    @pydantic.validator('description')
    def check_description(cls, value: str):
        if len(value) > 400:
            raise ValueError('description must be less than 400 chars')
        return value

    @pydantic.validator('owner')
    def check_owner(cls, value: str):
        if len(value) > 32:
            raise ValueError('owner_name must be less than 42 chars')
        return value


def validate(data_to_validate: dict, validation_class: Type[CreateAdSchema] | Type[PatchAdSchema]):
    try:
        return validation_class(**data_to_validate).dict(exclude_none=True)
    except pydantic.ValidationError as err:
        raise HttpError(400, err.errors())


def get_by_id(item_id: int, orm_model: Type[AdModel], session):
    orm_item = session.query(orm_model).get(item_id)
    if orm_item is None:
        raise HttpError(404, 'item not found')
    return orm_item


class AdView(MethodView):

    def get(self, ad_id: int):
        with Session() as session:
            ad = get_by_id(ad_id, AdModel, session)
            return jsonify({
                'header': ad.header,
                'creation': ad.creation_date.isoformat(),
                'owner': ad.owner,
                'description': ad.description
            })

    def post(self):
        json_data = request.json
        with Session() as session:
            try:
                new_ad = AdModel(**validate(json_data, CreateAdSchema))
                session.add(new_ad)
                session.commit()
            except IntegrityError:
                raise HttpError(409, 'ad already exists')
            return jsonify({'status': 'ok', 'id': new_ad.id})

    def patch(self, ad_id: int):
        data_to_patch = validate(request.json, PatchAdSchema)
        with Session() as session:
            ad = get_by_id(ad_id, AdModel, session)
            for field, value in data_to_patch.items():
                setattr(ad, field, value)
            session.commit()
            return jsonify({'status': 'success'})
        
    def delete(self, ad_id: int):
        with Session() as session:
            ad = get_by_id(ad_id, AdModel, session)
            session.delete(ad)
            session.commit()
            return jsonify({'status': 'success'})


app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ad'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/ads/', view_func=AdView.as_view('ads'), methods=['POST'])


app.run()
