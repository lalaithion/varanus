import configparser, sys, os
from twilio.rest import Client
import sendAlert

global account_sid
global auth_token
global emailFrom
global emailPass
global emailTo

def getConf():
    config=configparser.ConfigParser()
    config.read('./varanus.cfg')

    ##Add Twilio
    if (config['PHONE']['account_sid']):
        global account_sid
        global auth_token
        account_sid=config['PHONE']['account_sid']
        auth_token=config['PHONE']['auth_token']
    ##Add Email
    if (config['EMAIL']['EmailFrom']):
        global emailFrom
        global emailPass
        emailFrom=config['EMAIL']['EmailFrom']
        emailPass=config['EMAIL']['EmailPass']

def newTexts():
    getConf()
    print(account_sid, auth_token)
    client = Client(account_sid, auth_token)

    mes = 0
    for sms in client.messages.list(): #checks if messaged
        #print(sms.to)
        mes += 1

    return mes

def newCalls():
    getConf()
    client = Client(account_sid, auth_token)

    mes = 0
    for calls in client.calls.list():
        mes += 1

    return mes
