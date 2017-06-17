import boto3
import json
import decimal
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


def jenkins_config(event, context):
    print(event)
    
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    
    table = dynamodb.Table('jenkins_job_profile')
    
    pe = "job_name"
    jobs = []
    response = table.scan(
        ProjectionExpression=pe,
    )
    
    for i in response['Items']:
        jobs.append(i['job_name'])
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(
            ProjectionExpression=pe,
            FilterExpression=fe,
            ExpressionAttributeNames= ean,
            ExclusiveStartKey=response['LastEvaluatedKey']
            )
    
        for i in response['Items']:
            jobs.append(i['job_name'])
            
    print(jobs)
    responseString = "The jobs configured are: "
    for i in jobs:
        responseString += i+", "
    responseString = responseString[:-2]   
    print(responseString)
    
    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": responseString
            }
        }
    }