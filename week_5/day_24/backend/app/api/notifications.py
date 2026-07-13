from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.crud.notification_crud import create_notification, get_notification
from app.database import get_db
from app.schemas.notifications_schemas import notification_create, notification_response
from app.sse.sse_manager import broadcast_notification, stream
from sse_starlette.sse import EventSourceResponse

noti_router = APIRouter(prefix="/notifications", tags=["notifications"])


@noti_router.get("", response_model=notification_response | None, status_code=status.HTTP_200_OK)
def get_notifications(db: Session = Depends(get_db)):
    return get_notification(db)


@noti_router.post("", response_model=notification_response, status_code=status.HTTP_201_CREATED)
def post_notification(notification_data: notification_create, db: Session = Depends(get_db)):
    notification = create_notification(db, notification_data)
    broadcast_notification(notification)
    return notification


@noti_router.get("/stream")
def stream_notifications():
    return EventSourceResponse(stream())