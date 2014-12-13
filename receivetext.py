import webapp2
import cgi
import urllib
import urllib2
from twilio import twiml
import sys
import os
from keys import *

import json
import keys

class ReceiveText(webapp2.RequestHandler):
	def post(self):
		fromNumber = cgi.escape(self.request.get('From'))
		dataurl = "https://data.sparkfun.com/output/"+pubKey+".json"
		request = urllib2.Request(dataurl)
		result = urllib2.urlopen(request)
		jsonString = result.read()
		response = self.getPeopleStatus(self, jsonString)

		response = '\n' + response
		print response

		r = twiml.Response()
		try:
			r.message(response)	
		except:
			r.message(str(json_result))
		self.response.headers['Content-Type'] = 'text/xml'
		self.response.write(str(r))

	@staticmethod
	def getPeopleStatus(self, jsonString):
		jsonObj = json.loads(jsonString)
		#Get the last 5 minutes of data, or the entire list, whichever is smaller
		length = min (20, len(jsonObj))
		#Dictionary and associated amount of times active in last 10 minutes
		d_status = {}

		#Iterate through all 40 data points
		for x in range (0, length-1):
			#Iterate through dictionary keys to get status of people
			for key in jsonObj[x]:
				#Skip timestamps
				if key != "timestamp":
					#Create a new 
					if key not in d_status:
						#Add new person
						d_status[key] = int(jsonObj[x][key])
					else:
						#Add to person's active time
						d_status[key] += int(jsonObj[x][key])
		response = self.constructResponse(self, d_status)

		return response


	@staticmethod
	def constructResponse(self, d_status):
		activePeople = []
		for key in d_status:
			if d_status[key] != 0:
				#Append to array people that have been active in the past 10 minutes
				activePeople.append(key)


		response = "These people have been active in the house in the past minute: \n"
		for peeps in activePeople:
			response+=(peeps + "\n")

		return response
