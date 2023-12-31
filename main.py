from AsyncLogger import AsyncLogCollector
import valquest

# -- FRIENDS --
# userfriends/add/{nameTag}  - Add friend
# userfriends/cancel/{nameTag}  - Cancel outgoing friend request
# userfriends/decline/{nameTag}  - Decline friend request
# userfriends/remove/{nameTag}  - Remove a friend

async def add_friend(token:str, name:str, tag:str):
    status = await valquest.authenticated_request("POST", f"userfriends/add/{name}%23{tag}", token)
    if int(status[0]) == 201: return True
    else: return False

async def cancel_friend(token:str, name:str, tag:str):
    status = await valquest.authenticated_request("POST", f"userfriends/cancel/{name}%23{tag}", token)
    if int(status[0]) == 200: return True
    else: return False

async def decline_friend(token:str, name:str, tag:str):
    status = await valquest.authenticated_request("POST", f"userfriends/decline/{name}%23{tag}", token)
    if int(status[0]) == 200: return True
    else: return False

async def remove_friend(token:str, name:str, tag:str):
    status = await valquest.authenticated_request("POST", f"userfriends/remove/{name}%23{tag}", token)
    if int(status[0]) == 200: return True
    else: return False    

# -- PLANETS --
# planets/{planetId}/discover - Join planet
# planets/discoverable  - Returns all discoverable planets
# planets/{planetId}/invites  - Returns all active invites for the planet
# users/self/planets  - Get all joined planets
# users/self/planetIds  - Refresh joined planets

# -- SUBSCRIPTIONS --
# subscriptions/{subscriptionType}/price  - Get the price of Valour subscription
# subscriptions/{subscriptionType}/start  - Start a Valour subscription if valid credit amount
# subscriptions/active/{SelfId}  - Get the active subscription
# subscriptions/end  - End a Valour subscription

# -- NOTIFICATIONS --
# notifications/self/unread/all  - Retrieve all unread notifications
# notifications/self/{notificationId}/read/{booleanValue}  - Mark notification as read
# notifications/self/clear  - Clear all notifications

# -- MESSAGES --
# channels/{channelId}/typing  - Show that you're typing
# channels/direct/self  - Get all active Direct Message channels
# channels/{channelId}/messages  - Get all messages sent to a channel
# channels/{channelId}  - Send a message to the specified channel
# channels/{channelId}/messages/{messageId}  - Edit a message
# channels/{channelId}/messages/{messageId}  - Delete a message
# users/self/statedata  - Retrieve channel states

async def show_typing(token:str, channelId:int):
    status = await valquest.authenticated_request("POST", f"channels/{channelId}/typing", token)
    if int(status[0]) == 200: return True
    else: return False 

# -- TENOR --
# users/self/tenorfavorites  - Get all favorited Tenor GIFs

# -- SELF --
# users/self/compliance/{birthday}/{locality}  - Set the locality and birthday for the user
# users/token  - Get authenticated Valour user token
# users/self  - Get the authenticated user 
# users/self/referrals  - Get referrals


# -- NODES --
# node/name  - Get a primary node identity
# permissionsnodes/all/{planetId}  - Get the permission nodes for a planet

# -- ECONOMY --
# eco/accounts/self  - Retrieve economy accounts

# -- MODERATION --
# bans (IssuerId), (PlanetId), (TargetId), (Reason), (TimeCreated), (TimeExpires, null = perma)  - Issue a ban
# users/self/hardDelete  - Delete the authenticated user