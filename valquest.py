# Manages all Valour requests in one neat, little area!
from AsyncLogger import AsyncLogCollector
import aiohttp

logs = AsyncLogCollector()
node = None
BaseAddress = "https://app.valour.gg/api/"

async def retrieve_node(): # Returns the node name, needed for an authenticated_request
    async with aiohttp.ClientSession() as main_session:
        try:
            async with main_session.request("GET", "https://app.valour.gg/api/node/name") as resp:
                return await resp.text() # Hackish way of going about this, returns .text() even when != 200
        except Exception as e:
            await logs.error(f"An unexpected error occurred during retrieve_node: {e}")
            return -1

async def authenticated_request(method, url, token, **kwargs): # Returns the status code and response (text/json)
    global node
    while node == -1 or node == None: node = await retrieve_node() # Generally only ran at first initialization
    if token: headers = {"authorization": token, "x-server-select": node}
    else: headers={"x-server-select": node}
    async with aiohttp.ClientSession(headers=headers) as main_session:
        try:
            async with main_session.request(method, BaseAddress + url, **kwargs) as resp:
                if 'application/json' in resp.headers.get('Content-Type', ''):
                    return resp.status, await resp.json()
                return resp.status, None
        except Exception as e:
            await logs.error(f"An unexpected error occurred during authenticated_request: {e}")
            return -1, -1