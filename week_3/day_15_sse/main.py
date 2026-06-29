from fastapi import FastAPI,HTTPException
from app.routers.notification import userRouter

app = FastAPI()
app.include_router(userRouter)