'''
    Project Name :- Random password Generator

    Project Description :- This project generate a random password using python and send the password to gmail and Using EmailMessage we can gives the mail details.

'''



import random
import smtplib
from email.message import EmailMessage
import sqlite3 as sql

conn = sql.connect('mydb2.db')
cursor = conn.cursor()

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

email=input("Enter your email: ")

cursor.execute('''SELECT email from mailpwd''')
allmail=cursor.fetchall()
counter=0
for row in allmail:
    if row[0]==email:
            counter+=1

if counter==1:
    n=int(input("Enter the length of password:"))

    password = generatePassword(n)

    sql = '''UPDATE mailpwd SET PASSWORD='{}' WHERE EMAIL = '{}' '''.format(password,email)
    cursor.execute(sql)
    print("New password is updated successfully!!!")
    
else:
     print("Email Doesnot exist \nDo you want to add New email into database")
     add_to_db=input("If yes type Y otherwsie N:")
     if add_to_db=='Y' or add_to_db=='y':
        n=int(input("Enter the length of password:"))
        password = generatePassword(n)
        insert='''INSERT INTO mailpwd VALUES('{}','{}') '''.format(email,password)
        cursor.execute(insert)
        print("Data Added successfully!!!")

conn.commit()
conn.close()



sender = "pgtest122@gmail.com"
receiver = email

message = f"""\
Subject: your new password
To: {receiver}
From: {sender}

Hi user,
Your new password is - {password}"""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("4f7e2509c9db93", "932c3449ea967e")
    server.sendmail(sender, receiver, message)
