from twilio.rest import Client
from authTokens import account_sid, auth_token


def newCalls():
	client = Client(account_sid, auth_token)

	mes = 0
	for calls in client.calls.list():
	    mes += 1

	return mes
