from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config import DB_DSN

engine = create_async_engine(DB_DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
