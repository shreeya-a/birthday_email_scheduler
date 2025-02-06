# birthday_email_automator

# Birthday Email Automator
# Objective: Send automated birthday wishes to friends and family.
# Tasks:
# Use a CSV file or dictionary to store names, birthdays, and email addresses.
# Check the current date and match it to birthdays.
# Use smtplib to send a personalized birthday wish email.
# Automate the script to run daily with schedule.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# import pandas as pd
import csv
from datetime import date

today = date.today()
month = today.strftime("%m")
print(month)



Birthday_File = "./Birthday_Tracker.csv"


def send_birthday_email(name, email):
    sender_email = "shreeyadhikari11@gmail.com"
    receiver_email = email
    password = "qurm wfoz bhse jdzb"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "A warm birthday wish"
    
    body = f"""
    Dearest {name},

    Wishing you a very very Happy Birthday!
    Best wishes for all your future endeavour.
    
    

        """
    message.attach(MIMEText(body, "plain"))
    
    # send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    
    
  

try:
    with open(Birthday_File, mode= 'r', newline="") as file:
        reader = csv.DictReader(file)
        for data in reader:
            if data["BirthDay"][5:7] == month:
                name = data["Name"]
                email = data["Email"]
                print(name, email)
                send_birthday_email(name, email)
            
            
        
except Exception as e:
    print(f"Error:{e}")
            

