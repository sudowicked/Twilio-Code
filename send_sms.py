# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client	

# Find your Account SID and Auth Token at twilio.com/console

account_sid = 'AC02b350c07e80ff5a2e55730d0c5e11ec'
auth_token = 'f7cab49f8f5f4fee0d838f1833139231'
client = Client(account_sid, auth_token)


message = client.messages.create (
                body='Hi from twilio-python!',
                from_='+19704473904',
                to='+306972361896'
            )
