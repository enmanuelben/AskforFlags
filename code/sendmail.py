import os
import smtplib
import imghdr
from email.message import EmailMessage
import re

EMAIL_ADDRESS = 'email'
EMAIL_PASSWORD = 'password'

firstname = 'firstname'
lastname = 'lastname'
address = 'address'
town = 'town'
zip = 'zip'
state = 'state'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	with open("test.txt") as fp:
		line = fp.readline()
		while(line):
			linesplit = re.split(r'\t+', line)
			print(linesplit[0] + " : " + linesplit[1])
			msg = EmailMessage()
			msg['Subject'] = 'A request from a friend who loves your country'
			msg['From'] = EMAIL_ADDRESS
			msg.set_content('Dear, representatives of ' + linesplit[0] + '.\n\n My name is '+ firstname + ' ' + lastname +'. I love traveling from a very young age and I‘ve always wanted to every country, discover new cultures, and meet new amazing people. Even my dream has always been to be an ambassador, just like you! \n\n I want to collect everything related to ' + linesplit[0] + ' , I mean, your beautiful country. :) \n It would mean the world to me if you could send me a flag (even just a small one would be nice), a photo of your head of state, or just whatever you want related to your country.\n\nIf possible, could you please send to: \n\n'+ firstname + ' ' + lastname +'\n'+ address + '\n' + town + ',' + state + ' ' + zip + '\n\n Thank you,\n' + firstname)
			msg['To'] = linesplit[1]
			line = fp.readline()		
			smtp.send_message(msg)