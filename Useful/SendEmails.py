import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['email1', 'email2']

msg = EmailMessage()
msg['Subject'] = 'Here comes the subject of the email'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts

msg.set_content('This is just a test email V1')

""" 
#add an attachment to the email : 
with open('file', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)

"""

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
