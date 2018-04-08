#! /usr/local/bin/python3

import smtplib, subprocess, time, signal, sys, configparser
from ciscosparkapi import CiscoSparkAPI
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

global email
global phone
global spark
global account_sid
global auth_token
global phoneTo
global phoneFrom
global emailFrom
global emailPass
global emailTo
global SparkApiKey
global SparkApi
global roomName
global roomID

#Check which alerts we have configured
def getConf():
    config=configparser.ConfigParser()
    config.read('./varanus.cfg')

    ##Add Twilio
    if (config['PHONE']['account_sid']):
        global phone
        global phoneTo
        global phoneFrom
        global account_sid
        global auth_token
        account_sid=config['PHONE']['account_sid']
        auth_token=config['PHONE']['auth_token']
        phoneTo=config['PHONE']['PhoneTo']
        phoneFrom=config['PHONE']['PhoneFrom']
        phone = True
    ##Add Email
    if (config['EMAIL']['EmailFrom']):
        global emailFrom
        global emailPass
        global emailTo
        global email
        emailFrom=config['EMAIL']['EmailFrom']
        emailPass=config['EMAIL']['EmailPass']
        emailTo=config['EMAIL']['EmailAlert']
        email = True

    ##Add Spark
    if (config['SPARK']['Room']):
        global SparkApiKey
        global SparkApi
        global roomName
        global roomID
        global spark
        SparkApiKey=config['SPARK']['SparkKey']
        SparkApi=CiscoSparkAPI(access_token=SparkApiKey)
        roomName=config['SPARK']['Room']
        roomID=getRoomID(SparkApi,roomName)
        spark = True

def alert(msg, number):
    getConf()
    if spark:
        print("Alerting Spark Room")
        sparkMsg(msg, number)
    if email:
        print("Sending Alert Email")
        sendEmail(msg, number)
    if phone:
        print("Sending Alert Text Message")
        sendTxt(msg, number)

def sendTxt(msg, number):
    client = Client(account_sid, auth_token)
    client.messages.create(
        to=phoneTo,
        from_=phoneFrom,
        body=msg + str(number)
    )
    

def sendEmail(alertMsg, number):
	smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
	smtpserver.ehlo()  # Says 'hello' to the server
	smtpserver.starttls()  # Start TLS encryption
	smtpserver.ehlo()

	smtpserver.login(emailFrom, emailPass)  # Log in to server
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "ALERT!"
	msg['From'] = emailFrom
	msg['To'] = emailTo
	
	# Create the body of the message (a plain-text and an HTML version).
	text = alertMsg + str(number)
	
	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	
	msg.attach(part1)
	
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	smtpserver.sendmail(emailFrom, emailTo, msg.as_string())
	smtpserver.quit()
	

def sparkMsg(rsp, number):
#If we wanted to prompt response from chat room 
#        messages=api.messages.list(roomID)
#        for message in messages:
#            if "monitor" in message.text.lower():
#              if message.id != lastMessageID and message.created>lastMessageTime:
                  SparkApi.messages.create(roomID,text=rsp +  str(number))

def getRoomID(api, roomName):
    rawRooms=api.rooms.list()
    rooms=[room for room in rawRooms if room.title==roomName]
    if len(rooms)==0:
        api.rooms.create(roomName)
    for room in rooms: 
        roomID=(room.id)
        return roomID

