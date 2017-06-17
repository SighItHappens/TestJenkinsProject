import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
def authenticate_handler(event,context):
    print(event['username'])
    print(context)
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    table = dynamodb.Table('user_profile')
    username=event['username']
    password=event['password']
    try:
        response = table.get_item(
            Key={
                'user_id': username,
            }
        )
        print(response)
        if('Item' not in response):
            print(response)
            return { 
                "value":"false"
                }
        else:
            if(response['Item']['password']==password):
                return {"value":"true"}
            else:
                return {"value":"false"}
    except ClientError as e:
        print(e.response['Error']['Message'])
    return {"value":"false"}
    