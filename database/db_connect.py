from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from database.model import Base


engine = create_async_engine('sqlite+aiosqlite:///info.db')


async_session = sessionmaker(engine, class_=AsyncSession)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
