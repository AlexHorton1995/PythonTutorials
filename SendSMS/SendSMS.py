#!/usr/bin/python3

#libs
import datetime #date/time
from datetime import date #date lib
import os #access shutdown command
import pyautogui  #lib for writing to terminal
import time #lib to get the current time of day and date

#libs for the smtp email
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart

#get the current day, time
now = datetime.datetime.now()
theDay = now.day


email = "<youremail@email.com>"
pas = "<applicationpassword>"

sms_gateway = ["<smsemail@sms.com>","<ccdEmail@email.com>"]
# The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
# and port is also provided by the email provider.
smtp = "smtp.gmail.com" 
port = 587
# This will start our email server
server = smtplib.SMTP(smtp,port)
# Starting the server
server.starttls()
# Now we need to login
server.login(email,pas)

# Now we use the MIME module to structure our message.
msg = MIMEMultipart()
msg['From'] = email

# Make sure you add a new line in the subject
# Make sure you also add new lines to your body
# and then attach that body furthermore you can also send html content.

#permissions to log into the computer during a school day
if (now.hour >= 8 and now.hour <= 15) and (now.day >= 1 and now.day <=6):
    msg['Subject'] = "Rhiana has logged into the laptop for school\n"
    body = "Rhiana logged in at " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2) + "\n"
else:
    msg['Subject'] = "Rhiana has logged into the laptop!!!\n"
    body = "We can see you, on the laptop. You logged in at " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2) + " on the laptop.\n Shutting down computer now....\n"

msg.attach(MIMEText(body, 'plain'))

sms = msg.as_string()

server.sendmail(email,sms_gateway,sms)

# lastly quit the server
server.quit()

# finally, shut down the computer
os.system("x-terminal-emulator -e /bin/bash")
time.sleep(2)
pyautogui.typewrite("echo Congrats! You did exactly what we thought you were going to do!") 
pyautogui.press("enter")
time.sleep(2)
pyautogui.typewrite("echo Guess what is about to happen?") 
pyautogui.press("enter")
time.sleep(2)
pyautogui.typewrite("echo Emailing parents...") 
pyautogui.press("enter")
time.sleep(2)
pyautogui.typewrite("echo Texting Daddy...") 
pyautogui.press("enter")
time.sleep(2)
pyautogui.typewrite("echo And now we're shutting down the computer...") 
pyautogui.press("enter")
time.sleep(2)
pyautogui.typewrite("echo You are so busted...") 
pyautogui.press("enter")
time.sleep(1)

os.system("shutdown now")
