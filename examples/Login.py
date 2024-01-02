import pyvalour
import asyncio

async def main(email, password):
    try:
        token = await pyvalour.create_session(email, password) # create_session, or login, using our email and password
        # Returns token & user id if successful
        if token: # If it returns anything except False, it was successful
            print(f"Logged in! I'm user id {token[1]} with token {token[0]}")
            return 0
        else:
            print("Failed to sign in!")
            return -1
    except Exception as e:
        print("Failed!:", e)
        return -1

asyncio.run(main("email@domain.tld", "password123"))
