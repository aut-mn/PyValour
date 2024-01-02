import pyvalour
import asyncio


async def main(token):
    try:
        message_response = await pyvalour.send_text_message(token, 12215159187308546, 12215159187308544, 24559699131105280, "Hello from PyValour!") # Token, channelId, planetId (optional), authorMemberId (optional), and message
        # Returns boolean success value & the fingerprint for the message
        if message_response:
            print("Successfully sent message! Fingerprint: ", message_response[1])
            return 0
        else:
            print("Failed to send message!")
            return -1
    except Exception as e:
        print("Failed!:", e)
        return -1

asyncio.run(main('YOUR-TOKEN'))