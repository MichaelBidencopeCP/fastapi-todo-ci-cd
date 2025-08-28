from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from todo import models


async def create(db: AsyncSession, title: str, description: str):
    db_item = models.TodoItem(title=title, description=description)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

async def get_all(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(models.TodoItem).offset(skip).limit(limit)
    )
    return result.scalars().all()

