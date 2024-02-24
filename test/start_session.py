from src import session
import asyncio
import signal


class TestClient(session.Client):
    def __init__(self, token):
        super().__init__(token)



async def main():
    await client.start()
    await asyncio.sleep(30)
    await client.stop()

client = TestClient("ValourAuthToken")
loop = asyncio.new_event_loop()
loop.run_until_complete(main())
