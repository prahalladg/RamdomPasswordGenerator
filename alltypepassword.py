'''
    Project Name :- Random password Generator

    Project Description :- This project generate a random password using python and send the password to gmail.

'''


import random
import string
import smtplib

#to generate password
def get_password():
    random_source = string.ascii_letters + string.digits
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    

    # generate other characters
    for i in range(7):
        password += random.choice(random_source)
    
    password_list = list(password)
    # to shuffle characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

password= get_password()


sender = "pgtest1@gmail.com"
receiver = "pgtest122@gmail.com"

message = f"""\
Subject: your new password
To: {receiver}
From: {sender}

Hi user,
Your new password is - {password}"""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("4f7e2509c9db93", "932c3449ea967e")
    server.sendmail(sender, receiver, message)
