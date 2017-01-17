# TwtPy Lite
#		
# Andresito de Guzman
#
import twitter
import auth
    
api = twitter.Api(
        consumer_key=auth.consumer_key,
        consumer_secret=auth.consumer_secret,
        access_token_key=auth.access_token_key,
        access_token_secret=auth.access_token_secret
       )

person = api.VerifyCredentials()

## Tweet Silently (uses return instead of print [best for python programs])
def update(status):
    if status:
        s = api.PostUpdate(status)
        return s
    else:
        return "Error sending tweet"

## Tweet
def tweet(status):
	if(status == ""):
		return "Cannot tweet empty text"
	else:
		status = api.PostUpdate(status)
		return "You just tweeted: " + str(status.text)	

## Unfollow
def unfollow(username):
    if username:
        api.DestroyFriendship(screen_name=username)
        return "Unfollowed " + str(username)
    else:
        return "Username cannot be empty"
## Follow
def follow(username):
    if username:
        api.CreateFriendship(screen_name=username)
        return "Followed " + str(username)
    else:
        return "Username cannot be empty"

## Check your Name
def whoami():
	return "You are " + str(person.name)

## Check your Username/Screen Name
def username():
        return "Your username is @" + str(person.screen_name)

## Send a DM
def sendDM(to, message):
   if(to == ""):
      return "You cannot send a message to an empty recepient"
   else:
      if(message == ""):
         return "Message cannot be empty"
      else:
         api.PostDirectMessage(screen_name=to, text=message)
         return "DM Sent to " + str(to)