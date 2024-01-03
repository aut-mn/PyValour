# Manages all Valour requests in one neat, little area!
from AsyncLogger import AsyncLogCollector
import aiohttp
import datetime
import random, hashlib

logs = AsyncLogCollector()
node = None
BaseAddress = "https://app.valour.gg/api/"

async def retrieve_node(): # Returns the node name, needed for an authenticated_request
    async with aiohttp.ClientSession() as main_session:
        try:
            async with main_session.request("GET", "https://app.valour.gg/api/node/name") as resp:
                if resp.status == 200: return await resp.text()
                else: return None
        except Exception as e:
            await logs.error(f"An unexpected error occurred during retrieve_node: {e}")
            return None

async def authenticated_request(method, url, token, **kwargs): # Returns the status code and response (text/json)
    global node
    while node == None: node = await retrieve_node() # Generally only ran at first initialization
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
    
async def generate_unique_fingerprint(selfId:int, channelId:int): # Generates a random, unique fingerprint. Needed for sending messages.
     # This may look intimidating, but all it does is multiplies the current time to the selfId, generates a random number between 0 and the sum of that, and adds the channelId then the result is hashed
    unique_fingerprint = random.randint(0, int(str(selfId) + str(int(datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3])))) if isinstance(selfId, int) and isinstance(int(datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]), int) and channelId else None
    hashed_fingerprint = hashlib.sha256(str(unique_fingerprint).encode()).hexdigest() if unique_fingerprint is not None else None
    return hashed_fingerprint