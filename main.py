import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)  # gmail with port(localhost)

server.starttls()

# login with mail_id and password
server.login('me@gmail.com', 'password')

# receivers list
tolist = ["email1@gmail", "email2@gmail.com", "email3@gmail.com"]  # add up as many receivers you want 

# message to be sent
# here we can add To: with multiple email id's 
msg = '''\
From: Me@gmail.com
Subject: Testing EmailBot

This was a test run.

'''

server.sendmail('me@gmail.com', tolist, msg)  # here email to recipients of tolist will be sent in bcc
server.quit()
