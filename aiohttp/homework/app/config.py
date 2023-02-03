import os


DB_USER = os.getenv('PG_USER', 'test_user')
DB_PASSWORD = os.getenv('PG_PASSWORD', 'test_password')
DB_HOST = os.getenv('PG_HOST', '127.0.0.1')
DB_PORT = os.getenv('PG_PORT', '5431')
DB_NAME = os.getenv('PG_DB', 'test_db')


ASYNC_DSN = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
