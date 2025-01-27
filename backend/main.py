from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from db import database, Base
from routers import chats


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="My FastAPI App", version="1.0.0", lifespan=lifespan)

app.include_router(chats.router)


@app.get("/")
async def root():
    return {"status": "ok", "message": "API is up and running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
