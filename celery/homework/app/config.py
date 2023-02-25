import os

DB_USER = os.getenv("PG_USER")
DB_NAME = os.getenv("PG_DB")
DB_PASSWORD = os.getenv("PG_PASSWORD")
DB_HOST = os.getenv("PG_HOST")
DB_PORT = os.getenv("PG_PORT")

REDIS_DSN = os.getenv("REDIS_DSN")

MONGO_DSN = os.getenv("MONGO_DSN")

PG_DSN = os.getenv("PG_DSN")
