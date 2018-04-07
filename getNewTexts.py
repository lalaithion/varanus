from twilio.rest import Client

account_sid = "AC178822dcfff365d67db6913a640b0fb6"
auth_token = "3d73226d12c4c3c66f0ec454e23d3988"
client = Client(account_sid, auth_token)

for sms in client.messages.list():
    print(sms.to)