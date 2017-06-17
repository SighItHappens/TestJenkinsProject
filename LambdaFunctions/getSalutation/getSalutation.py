import datetime
from random import randint

def lambda_handler(event, context):
    
    response = []
    response.append("Hi, What can I help you with?")
    response.append("Hello, What can I help you with?")
    response.append("Hi, How may I help you?")
    randNum = randint(0,2)
    
    return {
      "dialogAction": {
        "type": "ElicitIntent",
        "message": {
          "contentType": "PlainText",
          "content": response[randNum]
        }
      }
    }
