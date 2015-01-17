#!/usr/bin/python

from twitter import *

def get_chunk(screen_name,cursor):
	followers = api.followers.ids(screen_name=screen_name, cursor=cursor)
	#print "next_cursor: " + str(followers[u'next_cursor'])
	next_cursor = followers[u'next_cursor']
	chunk = followers[u'ids']
	with open(screen_name + '_follower_ids.csv','a') as fileout:	
		for item in chunk:
			fileout.write(str(item) + ',')
		print "Wrote " + str(len(chunk)) + " ids"
		if (cursor == 0):
			return
		else:
			return get_chunk(screen_name, next_cursor)


#you may want to use your own values here in the future
parameters = {
    'grant_type':'client_credentials',
    'consumer_key':'sniwxLHfoimok5GN7g4OVxs2c',
    'consumer_secret':'HsdEdAeO1KA8NGtAXyZTc61kxzn0HNFMxMb59xCfEI7dnxOdQy',
    'access_token_key':'348067812-MsRhZFLOTcqcsJ3au7ZmFi7VZHwEbbR7QV5hvy2l',
    'access_token_secret':'yLZINjAZFa90s3vFu4TLKy7kn2wiRFrctApVEk9n6qZIx'}

bearer_token = oauth2_dance(parameters['consumer_key'],parameters['consumer_secret'])

try:
	print "Logging into twitter..."
	api = Twitter(auth=OAuth2(bearer_token=bearer_token), retry=True)
	print "Authenticated."
except:
	print "Unable to authenticate with twitter. Check access tokens."
	raise SystemExit

user = raw_input('Enter a username to get followers for: ')

cursor = -1

get_chunk(user, cursor)