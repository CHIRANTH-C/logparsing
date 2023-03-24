import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'chiranthchandrashekar123@gmail.com'
EMAIL_PASSWORD = 'cjwjvuyxhjcxnmzq'

msg = EmailMessage()
msg['Subject'] = 'Attaching the logs !'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('pfa attachment')

with open('report.txt','rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data,maintype='appplication',subtype='octet-stream', filename=file_name)


with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)