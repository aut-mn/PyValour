# This is the main library you import
from AsyncLogger import AsyncLogCollector
import valquest
import datetime
import random
import hashlib

# -- FRIENDS --
# userfriends/add/{nameTag}  - Add/accept friend
# userfriends/cancel/{nameTag}  - Cancel outgoing friend request
# userfriends/decline/{nameTag}  - Decline friend request
# userfriends/remove/{nameTag}  - Remove a friend
# users/{userId}/frienddata  - Retrieve incoming/outgoing/current friends
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

async def get_friend_data(token:str, userId:int): # Returns friend data JSON
    status = await valquest.authenticated_request("GET", f"users/{userId}/frienddata", token)
    if int(status[0]) == 200: return status[1]
    else: return False

# -- PLANETS --
# planets/{planetId}/discover - Join planet
# planets/{planetId}  - Update a planet
# planets/discoverable  - Returns all discoverable planets
# planets/{planetId}/invites  - Returns all active invites for the planet
# planets/{planetId}/roles  - Returns all roles for the planet
# users/self/planets  - Get all joined planets
# users/self/planetIds  - Refresh joined planets
async def get_joined_planets(token:str): # Returns joined planets JSON
    status = await valquest.authenticated_request("GET", f"users/self/planets", token)
    if int(status[0]) == 200: return status[1]
    else: return False

async def get_planet_roles(token:str, planetId:int): # Returns planet roles JSON
    status = await valquest.authenticated_request("GET", f"planets/{planetId}/roles", token)
    if int(status[0]) == 200: return status[1]
    else: return False

async def get_planet_channels(token:str, planetId:int): # Returns planet channels JSON
    status = await valquest.authenticated_request("GET", f"planets/{planetId}/channels", token)
    if int(status[0]) == 200: return status[1]
    else: return False

async def get_planet_members(token:str, planetId:int, pagination:int): # Returns planet members JSON, may be multiple pages but always starts with 0. All pages return at most 100 members.
    status = await valquest.authenticated_request("GET", f"planets/{planetId}/memberinfo?page={pagination}", token)
    if int(status[0]) == 200: return status[1]
    else: return False

async def update_planet(token:str, planetId:int, ownerId:int, description:str, discoverable:bool, iconUrl, name:str, public:bool, nsfw:bool): # If 200, returns pretty much the same data put in
    status = await valquest.authenticated_request("PUT", f"planets/{planetId}", token, json={"baseRoute":"api/planets","ownerId":ownerId,"name":name,"iconUrl":iconUrl,"description":description,"public":public,"discoverable":discoverable,"nsfw":nsfw,"id":planetId})
    if int(status[0]) == 200: return status[1]
    else: return False

# -- MEMBERS --
# members/{userId}/roles  - Returns the Role ID for the specified user
# userProfiles/{userId}  - Returns things like the headline, bio, etc.
async def get_user_profile(token:str, userId:int):
    status = await valquest.authenticated_request("GET", f"userProfiles/{userId}", token)
    if int(status[0]) == 200: return status[1]
    else: return False

# -- SUBSCRIPTIONS --
# subscriptions/{subscriptionType}/price  - Get the price of Valour subscription
# subscriptions/{subscriptionType}/start  - Start a Valour subscription if valid credit amount
# subscriptions/active/{SelfId}  - Get the active subscription
# subscriptions/end  - End a Valour subscription

# -- NOTIFICATIONS --
# notifications/self/unread/all  - Retrieve all unread notifications
# notifications/self/{notificationId}/read/{booleanValue}  - Mark notification as read
# notifications/self/clear  - Clear all notifications
async def get_unread_notifications(token:str): # Returns unread notifs JSON
    status = await valquest.authenticated_request("POST", f"self/unread/all", token)
    if int(status[0]) == 200: return status[1]
    else: return False 

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

async def get_direct_messages(token:str): # Returns DMs JSON
    status = await valquest.authenticated_request("GET", f"channels/direct/self", token)
    if int(status[0]) == 200: return status[1]
    else: return False 

async def delete_message(token:str, channelId:int, messageId:int):
    status = await valquest.authenticated_request("DELETE", f"channels/{channelId}/messages/{messageId}", token)
    if int(status[0]) == 200: return status[1]
    else: return False

async def send_text_message(token:str, channelId:int, planetId, authorMemberId, message:str): # Returns status & fingerprint
    try:
        selfId = await get_authenticated_user(token)
        if selfId: selfId = selfId['id']
        else: return False
        current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        # unique_fingerprint may look intimidating, but all it does is multiplies the current time to the selfId, generates a random number between 0 and the sum of that, and adds the channelId then the result is hashed
        unique_fingerprint = random.randint(0, int(str(selfId) + str(int(datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3])))) if isinstance(selfId, int) and isinstance(int(datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]), int) and channelId else None
        hashed_fingerprint = hashlib.sha256(str(unique_fingerprint).encode()).hexdigest() if unique_fingerprint is not None else None
        status = await valquest.authenticated_request("POST", f"channels/{channelId}/messages", token, json={"baseRoute":f"api/channels/{channelId}/messages","planetId":int(planetId),"replyToId":None,"authorUserId":selfId,"authorMemberId":int(authorMemberId),"content":message,"timeSent":current_time,"channelId":channelId,"embedData":None,"mentionsData":None,"attachmentsData":None,"fingerprint":hashed_fingerprint,"editedTime":None,"renderKey":None,"replyTo":None,"mentions":None,"embed":None,"attachments":None,"id":channelId})
        if int(status[0]) == 200: return True, hashed_fingerprint
        else: return False, hashed_fingerprint
    except Exception as e:
        return False, e

# -- TENOR --
# users/self/tenorfavorites  - Add favorite GIF
# users/self/tenorfavorites/{GIFId}  - DEKETE, remove a favorite GIF

# -- SELF --
# users/self/compliance/{birthday}/{locality}  - Set the locality and birthday for the user
# users/token  - Create a new token from an email & password
# users/self  - Get the authenticated user 
# users/self/referrals  - Get referrals
# users/register  - Create an account
async def create_session(email:str, password:str): # Creates a session and returns a token and userId
    status = await valquest.authenticated_request("POST", f"users/token", token=None, json={"email":email,"password":password})
    if int(status[0]) == 200: return status[1]['id'], status[1]['userId']
    else: return False

async def get_authenticated_user(token:str): # Returns authenticated json
    status = await valquest.authenticated_request("GET", f"users/self", token)
    if int(status[0]) == 200: return status[1]
    else: return False

async def update_profile(token:str, userId:int, animatedBorder:bool, backgroundImage:str, bio:str, borderColor:str, glowColor:str, headline:str, primaryColor:str, secondaryColor:str, tertiaryColor:str, textColor:str):
    status = await valquest.authenticated_request("PUT", f"userProfiles/{userId}", token, json={"baseRoute":"api/userProfiles","headline":headline,"bio":bio,"borderColor":borderColor,"glowColor":glowColor,"primaryColor":primaryColor,"secondaryColor":secondaryColor,"tertiaryColor":tertiaryColor,"textColor":textColor,"animatedBorder":animatedBorder,"backgroundImage":backgroundImage,"id":userId})
    if int(status[0]) == 200: return True
    else: return False

async def get_referrals(token:str):
    status = await valquest.authenticated_request("GET", f"users/self/referrals", token)
    if int(status[0]) == 200: return status[1]
    else: return False

async def create_account(username:str, email:str, password:str, DoB:str, referrer): # Creates an account. Yes. DoB is formatted YYYY-MM-DDTHH:MM:SS
    status = await valquest.authenticated_request("POST", f"users/register", token=None, json={"username":username,"email":email,"password":password,"referrer":referrer,"dateOfBirth":DoB,"locality":1,"inviteCode":"","source":""})
    if int(status[0]) == 200: return True
    else: return False

# -- NODES --
# node/name  - Get a primary node identity
# permissionsnodes/all/{planetId}  - Get the permission nodes for a planet

# -- ECONOMY --
# eco/accounts/self  - Retrieve economy accounts
# eco/accounts/self/global  - Retrieve user global account

# -- MODERATION --
# bans (IssuerId), (PlanetId), (TargetId), (Reason), (TimeCreated), (TimeExpires, null = perma)  - Issue a ban
# users/self/hardDelete  - Delete the authenticated user'