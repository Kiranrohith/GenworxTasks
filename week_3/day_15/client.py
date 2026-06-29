import asyncio
import websockets

async def send_messages(ws):
    name = input("Enter your name: ")
    print("start your chat: ")
    while True:
        message = await asyncio.to_thread(input)
        await ws.send(f"({name}) {message}")

async def receive_messages(ws):
    while True:
        message = await ws.recv()
        #print(f"\nServer: {message}")
        print(message)

async def main():
    async with websockets.connect("ws://localhost:8000/ws") as ws:
        await asyncio.gather(
            send_messages(ws),
            receive_messages(ws)
        )

asyncio.run(main())