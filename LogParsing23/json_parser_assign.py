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
    total_cart_cost = 0
    carts_data = read_data["carts"]
    for cart in carts_data:
        for product in cart["products"]:
            parsed_json.append((product["title"],product["quantity"]))
            total_cart_cost = total_cart_cost + int(product["total"])
    return parsed_json , total_cart_cost

# 3. Generate the report
def generate_report(parsed_json , total_cart_cost):
    report_file = open("report_for_carts_json.txt","w")
    entries = len(parsed_json)
    report_message = "The number of logs is: " + str(entries) + "\n"
    report_file.write(report_message)
    for log in parsed_json:
        report_file.write(str(log))
        report_file.write("\n")
    report_file.write("total cart cost : "+str(total_cart_cost))

def send_email(email_address,password,report1):
    EMAIL_ADDRESS = email_address
    EMAIL_PASSWORD = password

    msg = EmailMessage()
    msg['Subject'] = 'Attaching the logs of results from json_parser_assign.py file'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content('pfa attachment of json_parser_assign.txt log')

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

carts_json = read_json("carts.json")
parsed_json , total_cart_cost = parse_json(carts_json)
generate_report(parsed_json , total_cart_cost)
send_email('chiranthchandrashekar123@gmail.com','cjwjvuyxhjcxnmzq','report_for_carts_json.txt')