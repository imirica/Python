import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = "x"
EMAIL_PASSWORD = "Y"

contacts = ['email1', 'email2']

msg = EmailMessage()
msg['Subject'] = 'Seeking Wisdom and Guidance - Request for Mentorship'
msg['From'] = EMAIL_ADDRESS
msg.set_content("""test1""")

with open('your file', 'rb') as f:
    file_data = f.read()
    file_name = f.name

for contact in contacts:
    individual_msg = EmailMessage()
    individual_msg['Subject'] = msg['Subject']
    individual_msg['From'] = msg['From']
    individual_msg['To'] = contact
    individual_msg.set_content(msg.get_content())
    individual_msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(individual_msg)
        print(f"Sent to: {contact}")
