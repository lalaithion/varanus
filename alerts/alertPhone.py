from twilio.rest import Client
import sys
import os
# sys.path.append("../phone")
from phone.authTokens import account_sid, auth_token


def alertText():
	client = Client(account_sid, auth_token)
	client.messages.create(
	  to="+15716062372",
	  from_="+16027867186",
	  body="SOMEBODY TEXTING ME....HELP PLS"
	  )

def alertCall():
	client = Client(account_sid, auth_token)
	client.messages.create(
	  to="+15716062372",
	  from_="+16027867186",
	  body="SOMEBODY CALLING ME....HELP PLS"
	  )
