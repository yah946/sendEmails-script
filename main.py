from Attachment.motivation_letter_template import letter,string2pdf
from Attachment.email_template import message,MESSAGE_SUBJECT
from email.message import EmailMessage
from pypdf.errors import PdfReadError
from dotenv import load_dotenv
from pypdf import PdfReader
import pandas as pd
import subprocess
import itertools
import pyfiglet
import smtplib
import time
import sys
import os
# Progress Bar
def spinner(duration=5):
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    start = time.time()
    while time.time() - start < duration:
        sys.stdout.write("\r" + next(spinner) + " Wait a moment...\n")
        sys.stdout.flush()
        time.sleep(0.2)
# name of script
print(pyfiglet.figlet_format("sendEmails"))
# Loading variables from a .env file
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
CV_NAME = os.getenv('CV_FILE_NAME')
CV_PATH = os.path.join('Attachment',CV_NAME)
LETTER_NAME = os.getenv('LETTER_MOTIVATION_FILE_NAME')
LETTER_PATH = os.path.join('Attachment',LETTER_NAME)
# Reading CSV file
dataFrame = pd.read_csv('Attachment/emails.csv')
# Create a unique greating
def greating(gender,rh_name):
    if gender == 1:
        base = "Monsieur"
    elif gender == 2:
        base = "Madame"
    else:
        return "Monsieur, Madame,"
    if rh_name:
        return f"{base} {rh_name},"
    return f"{base},"
# Add Name of Company in the email and motivation letter
def companyName(name):
    if not pd.isna(name):
        name = name.lower()
        if(name[0]=='a' or
        name[0]=='o' or
        name[0]=='e' or
        name[0]=='i' or
        name[0]=='u'
        ):
            return f"d'{name.upper()}"
        else: return f"de {name.upper()}"
    else: return 'de votre entreprise'
# Add Attachment (Cv and Motivation Letter)
def add_attachment(path,msg):
    with open(path,'rb') as f:
        attach = f.read()
        file_name = os.path.basename(f.name)
        msg.add_attachment(attach,maintype='application',subtype='pdf',filename=file_name)
# Put together in the email (Subject, Body, and Attachment)
def create_email(recipient):
    msg = EmailMessage()
    msg['Subject'] = MESSAGE_SUBJECT
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient['email']
    salutation = greating(recipient['gender'],recipient['rh_name'])
    msg.set_content(message(salutation,companyName(recipient['company_name'])))
    string2pdf(letter(salutation,companyName(recipient['company_name'])))
    add_attachment(CV_PATH,msg)
    add_attachment(LETTER_PATH,msg)
    return msg
# Check the existence of CV in PDF format
try:
    PdfReader(CV_PATH)
except PdfReadError:
    print(f"invalid Cv file")
    exit()
except FileNotFoundError:
    print(f"Cv file not found")
    exit()
else:
    pass
# Sending Emails...
total = len(dataFrame)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    for i,row in dataFrame.iterrows():
        smtp.send_message(create_email(row))
        print('Message has been sent to:',row['email'])
        if i + 1<total:
            spinner(180)
print("Bye")