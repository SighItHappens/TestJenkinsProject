import requests
def chat_handler(event, context):
    r = requests.post("http://hackathonchatbot-hosting-mobilehub-643962401.s3-website-us-east-1.amazonaws.com/bot/HackathonJenkinsRun/alias/HackathonJenkins/user/homavta/text", data={'inputText': 'Hi'})
    print(r)
    return 'Hello from Lambda'