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
    client = Client(account_sid, auth_token)

    mes = []
    for sms in client.messages.list(): #checks if messaged
        mes.append(sms.from_)

    return len(mes), mes[len(mes)-1]

def newCalls():
    getConf()
    client = Client(account_sid, auth_token)

    mes = []
    for calls in client.calls.list():
        mes.append(calls.from_)

    return len(mes), mes[len(mes)-1]
