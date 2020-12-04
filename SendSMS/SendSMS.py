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

#lib to get the current user
import getpass

#get the current day, time, and user
now = datetime.datetime.now()
user = getpass.getuser()

canLogin = False
isAdmin = False

if user == "admin":
    isAdmin = True
    canLogin = True
elif (now.hour >= 7 and now.hour <= 15) and (now.day >= 1 and now.day <=6):
    canLogin = True
else:
    canLogin = False

email = "<replaceemail@email.com>" #replace with the credentialed email here
pas = "GMAILAPPPASSWORD" #get app password from google security settings

sms_gateway = ["EMAILONE@EMAIL.COM","EMAIL2@EMAIL.COM"] #put the emails you want to send to here

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
if not isAdmin:
    if canLogin:
        msg['Subject'] = "Kid has logged into the laptop for school\n"
        body = "Kid logged in at " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2) + "\n"
    else:
        msg['Subject'] = "Kid has logged into the laptop!!!\n"
        body = "We can see you, on the laptop. You logged in at " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2) + " on the laptop.\n Shutting down computer now....\n"
else:
    msg['Subject'] = "Testing!\n"
    body = "Testing Body of email at " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2) + " on the laptop.\n Shutting down computer now....\n"


msg.attach(MIMEText(body, 'plain'))

sms = msg.as_string()

server.sendmail(email,sms_gateway,sms)

# lastly quit the server
server.quit()

# finally, shut down the computer
if isAdmin:
    pyautogui.typewrite("clear")
    time.sleep(2)
    os.system("gnome-terminal -e /bin/bash")
    time.sleep(1)
    pyautogui.typewrite("gedit")
    pyautogui.press("enter")
    pyautogui.typewrite("Test completed, this is where the computer would shut down.")
    pyautogui.press("enter")
elif not canLogin:
    time.sleep(2)
    os.system("gnome-terminal -e /bin/bash")
    time.sleep(1)
    pyautogui.typewrite("gedit")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("Congrats! You did exactly what we thought you were going to do!") 
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("Guess what is about to happen?") 
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("Let's just send an email to your parents...") 
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("We'll also text Daddy...") 
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("And now we're shutting down the computer...") 
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.typewrite("You are so busted...") 
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("BUH BYE!!!") 
    pyautogui.press("enter")
    time.sleep(2)
    os.system("shutdown now")
else:
    os.system("/usr/bin/teams %U")
    print("Allowed...")