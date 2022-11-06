import smtplib 
from email import encoders
from email.minc.base import MIMEText
from email.mine.multibase import MIMEMultiport
from email.mine.txt import MIMEText

server = smtplib.SMTP("smtp gmail.com ",25)
server.ehlo()
with open("password.txt","r") as f:
    password = f.read()
server.login("rsathwik777@gmil.com",password)
msg =MIMEMultipart()
msg["from"] = "sathwik777@gmail.com"
msg["to"] = "cicada@gmail.com"
msg["subject"] = "hello there !!!!!"
with open("message.txt","r") as f:
    message = f.read()
msg.attach(MIMEText(message("plain")))


#photo

filename = "coding.jpg"
f = MIMEBase("application","octect-stram")
p.setpayload(attachment.read())
encoders.encode_base64(p)
p.add_header(f"content_dispostion",f"attachment+ filename{filename}")
msg.attach()
text =msg.as_string()
server.sendmail("gmail.com","rsathwik777@gmail.com",txt)