from twilio.rest import Client

from authTokens import account_sid, auth_token

client = Client(account_sid, auth_token)

client.messages.create( #Sends message
  to="+15716062372",
  from_="+16027867186",
  body="Test Post Please Ignore"
  )

for sms in client.messages.list(): #checks if messaged
    print(sms.to)
