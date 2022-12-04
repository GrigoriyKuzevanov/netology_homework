import pydantic
import os
import re
from sqlalchemy import Column, Integer, String, func, create_engine, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_bcrypt import Bcrypt

DSN = 'postgresql://test:1490@127.0.0.1:5431/test_db'

app = Flask('app')
bcrypt = Bcrypt(app)
Base = declarative_base()
# engine = create_engine(os.getenv('DSN'))
engine = create_engine(DSN)
session = sessionmaker(bind=engine)

password_regex = re.compile(
    "^(?=.*[a-z_])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&_])[A-Za-z\d@$!#%*?&_]{8,200}$"
)


class HttpError(Exception):
    def __init__(self, status_code: int, info: dict | list | str):
        self.status_code = status_code
        self.info = info


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify({
        'status': 'error',
        'message': error.message
    })
    response.status_code = error.status_code
    return response


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(32), nullable=False, unique=True)
    password = Column(String, nullable=True)


class AdModel(Base):
    __tablename__ = 'Ads'

    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False, unique=True)
    description = Column(String, nullable=False)
    creation_date = Column(Date, server_default=func.now())
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship(UserModel, lazy='joined')

Base.metadata.create_all(engine)


class CreateAdSchema(pydantic.BaseModel):
    pass


class AdView(MethodView):

    def get():
        pass

    def post():
        pass

    def delete():
        pass


app.add_url_rule('/ads/', view_func=AdView.as_view('ads'), methods=['POST'])
app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ad'), methods=['GET', 'DELETE'])

app.run()
