DB_USER = "test_user"
DB_PASSWORD = "test_password"
DB_HOST = "127.0.0.1"
DB_PORT = "5431"
DB_NAME = "test_db"

DB_DSN = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
