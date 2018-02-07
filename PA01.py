import tweepy
import json

consumer_key="Q"
consumer_secret="0"
access_token="1G"
access_token_secret="k"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

''' Task 1 '''

print("Task 1")
print("User 1")
u1 = api.get_user(34373370)
print("Screen Name:{}".format(u1.screen_name))
print("User Name:{}".format(u1.name))
print("User Location:{}".format(u1.location))
print("User Description:{}".format(u1.description))
print("The Number of Followers:{}".format(u1.followers_count))
print("The Number of Friends:{}".format(u1.friends_count))
print("The Number of statuses:{}".format(u1.statuses_count))
print("User URL:{}".format(u1.url))

print("\nUser 2")
u2 = api.get_user(26257166)
print("Screen Name:{}".format(u2.screen_name))
print("User Name:{}".format(u2.name))
print("User Location:{}".format(u2.location))
print("User Description:{}".format(u2.description))
print("The Number of Followers:{}".format(u2.followers_count))
print("The Number of Friends:{}".format(u2.friends_count))
print("The Number of statuses:{}".format(u2.statuses_count))
print("User URL:{}".format(u2.url))

print("\nUser3")
u3 = api.get_user(12579252)
print("Screen Name:{}".format(u3.screen_name))
print("User Name:{}".format(u3.name))
print("User Location:{}".format(u3.location))
print("User Description:{}".format(u3.description))
print("The Number of Followers:{}".format(u3.followers_count))
print("The Number of Friends:{}".format(u3.friends_count))
print("The Number of statuses:{}".format(u3.statuses_count))
print("User URL:{}".format(u3.url))



''' Part 2 '''
i = 0
print("Followers 1:")
for follower in tweepy.Cursor(api.followers,id=34373370,count=20).items():
	if (i<20):
		print(follower.screen_name)
		i=i+1
	if (i==20):
		break
i=0

print("\nFollowing 1:")
for following in tweepy.Cursor(api.friends,id=34373370,count=20).items():
        if (i<20):
                print(following.screen_name)
                i=i+1
        if (i==20):
                break
i=0

print("Followers 2:")
for follower in tweepy.Cursor(api.followers,id=26257166,count=20).items():
        if (i<20):
                print(follower.screen_name)
                i=i+1
        if (i==20):
                break
i=0



print("\nFollowing 2:")
for following in tweepy.Cursor(api.friends,id=26257166,count=20).items():
        if (i<20):
                print(following.screen_name)
                i=i+1
        if (i==20):
                break
i=0



print("Followers 3:")
for follower in tweepy.Cursor(api.followers,id=12579252,count=20).items():
        if (i<20):
                print(follower.screen_name)
                i=i+1
        if (i==20):
                break
i=0


print("\nFollowing 3:")
for following in tweepy.Cursor(api.friends,id=12579252,count=20).items():
        if (i<20):
                print(following.screen_name)
                i=i+1
        if (i==20):
                break
i=0





''' Part 3 '''
class FilteredStream(tweepy.StreamListener):
	def on_status(self,status):
		if 'Indiana' in status.text.lower():
			print(status.text)
		if 'weather' in status.text.lower():
			print(status.text)

streamListener = FilteredStream()
stream = tweepy.Stream(auth=api.auth,listener=streamListener)
while i < 50:
	stream.filter(locations=[-86.33,41.63,-86.20,41.74])
	i=i+1
