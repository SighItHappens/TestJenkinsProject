import requests
import json
import base64
from pprint import pprint

def getJiraStatus(event, context):

	user = event['currentIntent']['slots']['JIRAUser']
	print(user)

	url = "http://oncloud9.atlassian.net/rest/api/2/search?jql=assignee="+user

	password = base64.b64decode('SGFja2F0aG9uMQ==').decode('ascii')
	r = requests.get(url, auth=("siddhsu", password), headers={"content-type":"application/json"})
	issue = r.json()


	if('warningMessages' in issue):
		response = "There is no user called "+user
	elif(issue['total']==0):
		response = "There are no issues assigned to "+user
	else:
		response = "Issues assigned to "+user+" are:\n"

		for item in issue['issues']:
			response+=item['key']+' - '+item['fields']['issuetype']['name']+' - '+item['fields']['summary']+"\n"
			print(item['key']+' - '+item['fields']['issuetype']['name']+' - '+item['fields']['summary'])
	
	print(response)
	return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": response
            }
        }
    }