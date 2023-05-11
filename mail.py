import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "" //enter your mail id here
receiver_email = ""  //enter the receipants mail id
password = "" //enter your password

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "Enter the subject of mail here"

body = "Enter the body of the message"
message.attach(MIMEText(body, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_email, password)


text = message.as_string()
session.sendmail(sender_email, receiver_email, text)
session.quit()

print('Mail Sent')
