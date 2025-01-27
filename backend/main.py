from fastapi import FastAPI
from routers import chats
import uvicorn


app = FastAPI(title="My FastAPI App", 
              version="1.0.0")

app.include_router(chats.router)

@app.get("/")
async def root():
    return {"status": "ok", "message": "API is up and running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
