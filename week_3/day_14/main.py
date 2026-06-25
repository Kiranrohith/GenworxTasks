from fastapi import FastAPI
from base import Base
from database import engine
from routers import serviceRouter

app = FastAPI(title="Task Resource API")
app.include_router(serviceRouter)

Base.metadata.create_all(bind=engine)

