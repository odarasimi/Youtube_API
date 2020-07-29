import requests
import json
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from requests_oauthlib import OAuth2Session
'''
https://accounts.google.com/o/oauth2/v2/auth?
 scope=https://www.googleapis.com/auth/youtube.force-ssl&
 access_type=offline&
 include_granted_scopes=true&
 response_type=code&
 state=state_parameter_passthrough_value&
 redirect_uri=http://localhost&
 client_id=


#my-project-youtube-278602

curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=authorization_code&code=&redirect_uri=http://localhost&client_id=&client_secret=" https://accounts.google.com/o/oauth2/token
https://www.googleapis.com/oauth2/v4/token
'''
parameters = {"key":"","maxResults":"200", "access_token":"", "part": ["snippet"] , "mine": "True"}
baseurl = "https://www.googleapis.com/youtube/v3/subscriptions"
response = requests.get(baseurl, params = parameters)
responses = response.json()
results = []
for keyd in responses:
	if keyd == "items":
		for i in range(len(responses[keyd])):
			result = (responses[keyd][i]["snippet"]["title"]).encode("utf-8")
			results.append(result)
print (results)

for item in results:
	parameters = {"key":"","maxResults":"200", "access_token":"", "part": ["snippet"] , "forUsername"}
	baseurl = "https://www.googleapis.com/youtube/v3/subscriptions"
	response = requests.get(baseurl, params = parameters)
	responses = response.json()
	results = []
	for keyd in responses:
		if keyd == "items":
			for i in range(len(responses[keyd])):
				result = (responses[keyd][i]["snippet"]["title"]).encode("utf-8")
				results.append(result)
	print (results)



'''
class Youtube():Bearer [YOUR_ACCESS_TOKEN]'
	"""docstring for getYoutube"""
	url = "https://www.googleapis.com/youtube/v3/"
	auth = ""

	def __init__(self, endpoint, type):
		self.type = type
		self.endpoint = endpoint
		self.baseurl = url + endpoint
		self.key = auth
		
	def __str__(self):
		return "{}: {}".format(self.type, self.baseurl)


class getTrending(Youtube):
	part = ["snippet"]
	chart = "mostPopular"

	def __init__(self, endpoint, type, regionCode = "ng"):
		self.regionCode = regionCode
		self.type = type
		self.endpoint = endpoint
		self.baseurl = Youtube.url+endpoint

	def get3trending(self):
		parameters = {"key": self.auth, "part": self.part , "chart": self.chart, "regionCode": self.regionCode}
		response = requests.get(self.baseurl, params = parameters)
		responses = response.json()
		results = []
		for keyd in responses:
			if keyd == "items":
				for i in range(len(responses[keyd])):
					result = (responses[keyd][i]["snippet"]["title"]).encode("utf-8")
					results.append(result)
		print (results)
		return (results)
				

'''