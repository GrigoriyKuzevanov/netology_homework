import os

DB_USER = os.getenv('PG_USER')
DB_NAME = os.getenv('PG_DB')
DB_PASSWORD = os.getenv('PG_PASSWORD')
DB_HOST = os.getenv('PG_HOST')
DB_PORT = os.getenv('PG_PORT')

REDIS_DSN = os.getenv('REDIS_DSN')

PG_DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
