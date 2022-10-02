from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://meshdb_user:Boqgg3dljhOPzTFDl4aA2W8aoxnXAGzw@dpg-ccrieq9a6gdl22bkim20-a.oregon-postgres.render.com/meshdb"
ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://meshdb_user:Boqgg3dljhOPzTFDl4aA2W8aoxnXAGzw@dpg-ccrieq9a6gdl22bkim20-a.oregon-postgres.render.com/meshdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)
AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
