import datetime
import asyncio
from app.models import Notification

client = []

async def stream():
    notification_queue = asyncio.Queue()
    client.append(notification_queue)

    try:
        while True:
            message = await notification_queue.get()

            yield f"data: {message}\n\n"
    finally:
        client.remove(notification_queue)

async def notify(notification, db):
    notif = Notification(message=notification.message)
    db.add(notif)
    db.commit()
    db.refresh(notif)

    for queue in client:
        await queue.put(notification.message)

    return {
        "status": "Notification Sent",
        "id": notif.id,
        "message": notif.message,
        "created_at": notif.created_at,
    }