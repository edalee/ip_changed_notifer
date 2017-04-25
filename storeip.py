import urllib, re, os, smtplib 
from email_config import *

# Check file to exists if not create it to store ip address  
filename = 'current_ip.txt'
if not os.path.isfile(filename):
	file(filename, 'w').close()

# Get your current ip 
current_ip = re.search('"([0-9.]*)"', urllib.urlopen("http://ip.jsontest.com/").read()).group(1)

# Open stored ip address
stored_ip = open(filename)
read_ip = stored_ip.read()
stored_ip.close()

# test
# current_ip = "201.2.64.06"

message = "\r\n".join(["From: <email_address>",
"To: <email_address>",
"Subject: ip Change",
"",
"Your ip address has changed.\nNew ip address is %s" % current_ip
])

# Check stored address against current address
if read_ip == current_ip:
	print("ip not changed")
	print(read_ip)
else:
	print("ip has changed")
	print(current_ip)
	write_ip = open(filename, 'w')
	write_ip.write(current_ip)
	write_ip.close()
	try:
		server.ehlo()
		server.starttls()
		server.login(username,password)
		server.sendmail(sender, receiver, message)
		print("Successfully sent")
	except:
		print"Error: unable to send mail"
