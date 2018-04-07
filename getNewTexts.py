from twilio.rest import Client

token = []
with open("../auth.txt", "r") as f:
		for line in f:
			token.append(line.strip())

account_sid = token[0]
auth_token = token[1]

client = Client(account_sid, auth_token)

for sms in client.messages.list():
    print(sms.to)