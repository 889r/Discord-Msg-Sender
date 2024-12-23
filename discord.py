import requests
from terminut import log

url = "" #enter url from requests

data = {
    "content": "@everyone" #message you want to send
}

headers = {
    "authorization": "", #authorization
    "connection": "keep-alive"
}


# Uncomment this block to send only 1 message
#response = requests.post(url=url, data=data, headers=headers)
#if response.status_code == 200:
#    log.info("Message Sent Sucessfully!")
#else:
#    log.error("Failed To Send Message")


# Uncomment this block to spam messages:
#while True:
#    response = requests.post(url=url, data=data, headers=headers)
#    if response.status_code == 200:
#        log.info("Message Send Sucessfully!")
#    else:
#        log.error("Failed Sending Message")



#t.me/TonyQarri
