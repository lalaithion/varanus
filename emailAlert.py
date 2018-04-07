#Josh Anderson
import smtplib, subprocess, time, signal, sys, configparser
from ciscosparkapi import CiscoSparkAPI
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
email = False
phone = False
spark = False
account_sid=""
auth_token=""
emailFrom=""
emailPass=""
emailTo=""
SparkApiKey=""
SparkApi=""
roomName=""
roomID=""

#Check which alerts we have configured
def getConf():
    config=configparser.ConfigParser()
    config.read('./varanus.cfg')

    ##Add Twilio
    if (config['PHONE']['account_sid']):
        account_sid=config['PHONE']['account_sid']
        auth_token=config['PHONE']['auth_token']
        phone = True

    ##Add Email
    if (config['EMAIL']['EmailFrom']):
        emailFrom=config['EMAIL']['EmailFrom']
        emailPass=config['EMAIL']['EmailPass']
        emailTo=config['EMAIL']['EmailAlert']
        email = True

    ##Add Spark
    if (config['SPARK']['Room']):
        SparkApiKey=config['SPARK']['SparkKey']
        SparkApi=CiscoSparkAPI(access_token=SparkApiKey)
        roomName=config['SPARK']['Room']
        roomID=getRoomID(SparkApi,roomName)
        spark = True

def alert():
    startTime=time.time()
    if spark:
        sparkMsg()
    if email:
        email()


def email():
	smtpserver.ehlo()  # Says 'hello' to the server
	smtpserver.starttls()  # Start TLS encryption
	smtpserver.ehlo()
	print(type(emailFrom), type(emailPass))
	smtpserver.login(emailFrom, emailPass)  # Log in to server
	today = datetime.date.today()  # Get current time/date
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Link"
	msg['From'] = emailFrom
	msg['To'] = emailTo

	# Create the body of the message (a plain-text and an HTML version).
	text = "ALERT! There is a problem!"
	html = """\
	<html>
	  <head></head>
	  <body>
	    <p>ALERT!<br>
	       IT IS TIME TO PANIC!<br>
	    </p>
	  </body>
	</html>
	"""

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	smtpserver.sendmail(emailFrom, emailTo, msg.as_string())
	smtpserver.quit()


def sparkMsg():
#If we wanted to prompt response from chat room
#        messages=api.messages.list(roomID)
#        for message in messages:
#            if "monitor" in message.text.lower():
#              if message.id != lastMessageID and message.created>lastMessageTime:
                  rsp="ALERT! THERE IS A PROBLEM!!!!"
                  SparkApi.messages.create(roomID,text=rsp)

def getRoomID(api, roomName):
    rawRooms=api.rooms.list()
    rooms=[room for room in rawRooms if room.title==roomName]
    if len(rooms)==0:
        api.rooms.create(roomName)
    for room in rooms:
        roomID=(room.id)
        return roomID

getConf()
alert()
