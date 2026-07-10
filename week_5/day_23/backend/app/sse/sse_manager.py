import asyncio
import json

clients = []


async def stream():
    print("Client connected")

    queue = asyncio.Queue()
    clients.append(queue)
    print(f"Connected clients: {len(clients)}")
    try:
        while True:
            message = await queue.get()
            print("Sending:", message)
            yield f"data: {message}\n\n"
    finally:
        if queue in clients:
            clients.remove(queue)
            print("Client disconnected")


def broadcast_notification(notification):
    payload = json.dumps(
        {
            "not_id": notification.not_id,
            "title": notification.title,
            "server_message": notification.server_message,
            "not_type": notification.not_type,
            "created_at": notification.created_at.isoformat() if notification.created_at else None,
        }
    )

    for queue in list(clients):
        queue.put_nowait(payload)