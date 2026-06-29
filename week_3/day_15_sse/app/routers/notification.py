from fastapi import APIRouter, status, Depends
from app.crud import notify, stream
from fastapi.responses import StreamingResponse
from app.schemas import NotifyRequest
from app.database import get_db
from sqlalchemy.orm import Session

userRouter = APIRouter()

@userRouter.get("/notifications", status_code=200)
async def streaming():
    return StreamingResponse(stream(), media_type="text/event-stream")

@userRouter.post("/notify", status_code=200)
async def notifying(notification: NotifyRequest, db: Session = Depends(get_db)):
    return await notify(notification, db)