import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email():
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.subject = 'log file is here dun dun dun'

    def send(self):
        fp = open('log.txt')
        body = (fp.read())
        fromaddr = "peteratkinson1994@gmail.com"
        toaddr = "peteratkinson1994@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "SUBJECT OF THE MAIL"
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login('', '')
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
