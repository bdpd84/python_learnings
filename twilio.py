from twilio.rest import Client
import re
from selenium import webdriver

# Twilio Account SID and Authentication Token
account_sid = "ACa36611b0a2d3b1a50a2a8f0e7ed28199"
account_token = "31a2c3bc545a053471957cbe22f27f0e"

#Twilio connection creation
client = Client(account_sid, account_token)

#Fetch last received SMS
for sms in client.messages.list(limit=1):
     smsbody = sms.bodear
     print(smsbody)

#Extract Https URL only from the SMS Body
def find(smsbody):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?<<>>“”‘’]))"
    url = re.findall(regex,smsbody)
    return [x[0] for x in url]

#Strip additional characters in the Extracted URL
url = find(smsbody)
newurl = str(url)[2:-2]

#Open the URL in Chrome web browser using Selenium Webdriver
driver = webdriver.Chrome("C://Users/Anand/Desktop/test/chromedriver.exe")
driver.get(newurl)




