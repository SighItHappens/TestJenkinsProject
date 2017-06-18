import datetime
from random import randint

def lambda_handler(event, context):  
  print(event)
  
  response = []
  response.append("Hi, What can I help you with?")
  response.append("Hello, What can I help you with?")
  response.append("Hi, How may I help you?")
  response.append("Good day! How can I help?")
  randNum = randint(0,3)

  return {
    "dialogAction": {
      "type": "ElicitIntent",
      "message": {
        "contentType": "PlainText",
        "content": response[randNum]
      }
    }
  }