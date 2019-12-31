from celery import Celery
import simplejson
import pprint
import sys
import requests
import json

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def spotifyGet():
	f = open('creds.csv', "r")
	creds = f.read().split("\n") # "\r\n" if needed
	creds = creds[0].split(',')

	CLIENT_ID = creds[0]
	CLIENT_SECRET = creds[1]

	grant_type = 'client_credentials'
	body_params = {'grant_type' : grant_type}

	url='https://accounts.spotify.com/api/token'
	response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 

	token_raw = simplejson.loads(response.text)
	token = token_raw["access_token"]

	r = requests.get(url="https://api.spotify.com/v1/playlists/0pMhZErjSM54QidKptzAiX/tracks", headers=headers)
	tracks = json.loads(r.text)
	peep = tracks['items'][-1]['track']
	trackName = peep['name']
	artist = peep['artists'][-1]['name']
	print(trackName,'by',artist)
