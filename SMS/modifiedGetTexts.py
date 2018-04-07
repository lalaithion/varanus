from twilio.rest import Client

token = []
with open("../../auth.txt", "r") as f:
		for line in f:
			token.append(line.strip())

account_sid = token[0]
auth_token = token[1]

client = Client(account_sid, auth_token)

client.messages.create( #Sends message
  to="+15716062372",
  from_="+16027867186",
  body="Test Post Please Ignore"
  )

for sms in client.messages.list(): #checks if messaged
    print(sms.to)
