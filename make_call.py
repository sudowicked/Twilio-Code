import sys
import os
from twilio.rest import Client	

w = open('whitelist')
whitelist = w.readline()
b = open('blacklist')
blacklist = b.readline()

number = sys.argv[1]

if number in whitelist:
	account_sid = 'AC02b350c07e80ff5a2e55730d0c5e11ec'
	auth_token = 'f7cab49f8f5f4fee0d838f1833139231'
	client = Client(account_sid, auth_token)

	call = client.calls.create (
		url='https://handler.twilio.com/twiml/EH0dc5f12e969959be850c2c7de21940e4',
               	to=number,
               	from_='+19704473904'
	)
elif number in blacklist:
	account_sid = 'AC02b350c07e80ff5a2e55730d0c5e11ec'
	auth_token = 'f7cab49f8f5f4fee0d838f1833139231'
	client = Client(account_sid, auth_token)

	call = client.calls.create (
		url='https://handler.twilio.com/twiml/EH25e42b26edf7246451fb6831f07aa27e',
               	to=number,
               	from_='+19704473904'
	)
