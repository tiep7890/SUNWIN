import asyncio
import websockets
import json
import random
import time

current_session = 100000

async def send_fake_session(websocket, path):
    global current_session
    print(f"Client connected: {websocket.remote_address}")

    while True:
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        result = "Tài" if total >= 11 else "Xỉu"
        session_data = {
            "Phien": current_session,
            "Xuc_xac_1": dice[0],
            "Xuc_xac_2": dice[1],
            "Xuc_xac_3": dice[2],
            "Tong": total,
            "Ket_qua": result
        }
        await websocket.send(json.dumps(session_data))
        print(f"Gửi phiên {current_session} | {dice} => {total} ({result})")
        current_session += 1
        await asyncio.sleep(10)

start_server = websockets.serve(send_fake_session, "0.0.0.0", 8765)
print("🔥 Fake Sunwin server running at ws://localhost:8765")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()