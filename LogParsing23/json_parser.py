import json
import smtplib
from email.message import EmailMessage

# 1. Read the json file
def read_json(filename):
    read_file = open(filename,'r')
    read_json_string = read_file.read()
    data_json = json.loads(read_json_string)
    return data_json

# 2. Parse the Json
def parse_json(read_data):
    parsed_json = []
    users_data = read_data["users"]
    total_data = read_data["total"]
    for user in users_data:
        if user["address"]["city"]=="Washington":
            parsed_json.append((user["firstName"],user["lastName"],user["macAddress"]))
    return parsed_json

# 3. Generate the report
def generate_report(matched_logs):
    report_file = open("report_for_json.txt","w")
    entries = len(matched_logs)
    report_message = "The number of logs is: " + str(entries) + "\n"
    report_file.write(report_message)
    for log in matched_logs:
        report_file.write(str(log))
        report_file.write("\n")

def send_email(email_address,password,report1):
    EMAIL_ADDRESS = email_address
    EMAIL_PASSWORD = password

    msg = EmailMessage()
    msg['Subject'] = 'Attaching the logs of results from json_parser.py file'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content('pfa attachment of json_parser.txt log')

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

users_json = read_json("users.json")
parsed_json = parse_json(users_json)
generate_report(parsed_json)
send_email('user@email.com','password','report_for_json.txt')