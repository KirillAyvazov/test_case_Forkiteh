from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from router.info import router as reviews_router
from database.db_connect import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(title="Test case for Forkiteh", lifespan=lifespan)
app.include_router(reviews_router)


if __name__ == '__main__':
    uvicorn.run(app)
