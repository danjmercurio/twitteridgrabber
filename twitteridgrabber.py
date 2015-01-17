#!/usr/bin/python

from twitter import *
from credentials import parameters

def get_chunkCSV(api_object,screen_name,cursor):
	followers = api_object.followers.ids(screen_name=screen_name, cursor=cursor)
	next_cursor = followers[u'next_cursor']
	chunk = followers[u'ids']
	with open(screen_name + '_follower_ids.csv','a') as fileout:	
		for item in chunk:
			fileout.write(str(item) + ',')
		if len(chunk) > 0:
			print "Wrote " + str(len(chunk)) + " ids"
		if (next_cursor == 0):
			return
		else:
			return get_chunkCSV(api_object, screen_name, next_cursor)

def get_chunkList(api_object,screen_name,cursor,op_list):
	followers = api_object.followers.ids(screen_name=screen_name, cursor=cursor)
	next_cursor = followers[u'next_cursor']
	chunk = followers[u'ids']
	if (chunk and len(chunk) > 0):
		for item in chunk:
			op_list.append(item)
		return get_chunkList(api_object, screen_name, next_cursor, op_list)
	elif (next_cursor == 0):
		return op_list

def auth():
	bearer_token = oauth2_dance(parameters['consumer_key'],parameters['consumer_secret'])
	api = Twitter(auth=OAuth2(bearer_token=bearer_token), retry=True)
	return api



if __name__=='__main__':
	try:
		print "Logging into twitter..."
		api = auth()
		print "Authenticated."
	except:
		print "Unable to authenticate with twitter. Check access tokens."
		raise SystemExit

		user = raw_input('Enter a username to get followers for: ')

		cursor = -1

		get_chunkCSV(api, user, cursor)