#!/usr/bin/python

from twitter import *
from credentials import parameters

bearer_token = oauth2_dance(parameters['consumer_key'],parameters['consumer_secret'])
api = Twitter(auth=OAuth2(bearer_token=bearer_token), retry=True)


def get_chunkCSV(screen_name,api_object=api,cursor=-1):
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
			return get_chunkCSV(screen_name, api_object=api_object, cursor=next_cursor)

def get_chunkList(screen_name, api_object=api,cursor=-1,op_list=[]):
	followers = api_object.followers.ids(screen_name=screen_name, cursor=cursor)
	next_cursor = followers[u'next_cursor']
	chunk = followers[u'ids']
	if (chunk and len(chunk) > 0 and next_cursor not 0):
		for item in chunk:
			op_list.append(item)
		return get_chunkList(screen_name=screen_name, api_object=api_object, cursor=next_cursor, op_list=op_list)
	elif (next_cursor == 0):
		return op_list



if __name__=='__main__':
	print "Logged into twitter..."
	try:
		user = raw_input('Enter a username to get followers for: ')

		cursor = -1

		get_chunkCSV(api, user, cursor)
	except:
		print "Unable to authenticate with twitter. Check access tokens."
		raise SystemExit

