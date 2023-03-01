'''
    Project Name :- Random password Generator

    Project Description :- This project generate a random password using python and send the password to gmail and Using EmailMessage we can gives the mail details.

'''



import random
import smtplib
from email.message import EmailMessage

#to generate password
def generatePassword(n):
    """
    #Function to generate password
    """
    passwordconbination = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&*"
    password = ""

    for i in range(n):
        password += random.choice(passwordconbination)

    return password
#n=int(input("Enter the length of password:"))
n = 8
password = generatePassword(n)

# set your email and password
mail_ID = "pgtest122@gmail.com"
mail_Pwd = "jrjauxmoivzccgqs"                        #app password


mail_details = EmailMessage()
mail_details['Subject'] = "Here is your password"
mail_details['From'] = mail_ID
mail_details['To'] = "pgahir1045@gmail.com"
mail_details.set_content("Hi user,\n Your password is "+password)

# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(mail_ID, mail_Pwd)
    smtp.send_message(mail_details)