import re
import smtplib
from email.message import EmailMessage

# 1. Read the file
def read_logs(filepath):
    file_contents = open(filepath,'r')
    read_logs = file_contents.read()
    split_logs = read_logs.split('\n')
    file_contents.close()
    return split_logs
    
# 2. Match with regular expression
def parse_logs(logs,regexp):
    matched_logs = []
    for log_entry in logs:
        matches = re.match(regexp,log_entry)
        if matches:
            matched_groups = matches.groups()
            timestamp , func , process , message = matched_groups
            matched_logs.append((timestamp , func , process , message))
    return matched_logs

# 3. Generate the report
def generate_report(matched_logs):
    report_file = open("report_assignment.txt","w")
    entries = len(matched_logs)
    report_message = "The number of logs is: " + str(entries) + "\n"
    report_file.write(report_message)
    for log in matched_logs:
        report_file.write(str(log))
        report_file.write("\n")

# 4. Send the email of the report
def send_email(email_address,password,report1):
    EMAIL_ADDRESS = email_address
    EMAIL_PASSWORD = password

    msg = EmailMessage()
    msg['Subject'] = 'Attaching the logs of results from log_parser_asign.py file'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content('pfa attachment of report_assignment.txt log')

    files = [report1]
    for file in files:
        with open(file,'rb') as f:
            file_data = f.read()
            file_name = f.name      
        msg.add_attachment(file_data,maintype='appplication',subtype='octet-stream', filename=file_name)

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

        smtp.send_message(msg)


logs_list = read_logs("logs.txt")
found_logs = parse_logs(logs_list,regexp=r'(.*) ([I,W]) (ActivityManager): (.*)')
generate_report(found_logs)
send_email('chiranthchandrashekar123@gmail.com','cjwjvuyxhjcxnmzq','report_assignment.txt')