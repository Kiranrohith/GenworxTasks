from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from sse_starlette.sse import EventSourceResponse
import asyncio
from datetime import datetime

app = FastAPI()

connections = []

async def event_generator():

    while True:

        now = datetime.now()
        yield {
            "data": now.time()
        }

        await asyncio.sleep(1)

@app.get("/events")
async def events():
    return EventSourceResponse(event_generator())

@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):

    await websocket.accept()
    print("Client Connected!")

    connections.append(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            print(message)
            
            for connection in connections:
                    await connection.send_text("Client sent message: " + message)
    except WebSocketDisconnect:
        print("Client Disconnected")
        connections.remove(websocket)

