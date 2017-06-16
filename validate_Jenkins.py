import boto3
import json
import decimal
import requests
import jenkins
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def validate_Jenkins(event, context):
    print(event)
    
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    
    table = dynamodb.Table('jenkins_job_profile')
    
    jobName = event['currentIntent']['slots']['component']
    branchName = event['currentIntent']['slots']['branch']
    
    print(jobName)
    try:
        response = table.get_item(
            Key={
                'job_name': jobName,
            }
        )
        print(response)
        if('Item' not in response):
            print(response)
            return { 
                "dialogAction": {
                    "type": "ElicitSlot",
                    "message": {
                        "contentType": "PlainText",
                        "content": "The component has not been configured, please enter the right one."
                    },
                    "intentName": event['currentIntent']['name'],
                    "slots": event['currentIntent']['slots'],
                    "slotToElicit" : "component"
                }
            }
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        jenkinsJobName = item['jenkins_name_link']
        
        server = jenkins.Jenkins('http://52.86.233.190:8080', username='admin', password='admin')
        
        print(jenkinsJobName)
        print(branchName)
        
        server.build_job(jenkinsJobName, {'token': 'HackathonToken', 'branchName': branchName})
        
        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "A build has been initiated"
                }
            }
        }