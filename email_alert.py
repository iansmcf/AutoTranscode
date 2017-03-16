import smtplib

from email.mime.text import MIMEtext


# construct message
#msg['Subject'] = "Test alert"
#msg['From'] = "root"
#msg['To'] = "iansmcfarlane@gmail.com"

s = smtplib.SMTP('smtp.gmail.com')
s.sendmail("root","iansmcfarlane@gmail.com","aeuausd")
s.quit()
