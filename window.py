import turtle
import time
import random
from urllib3 import Retry

i = 1
while i == 1:
    wn = turtle.Screen()
    wn.title("Password Identifier")
    wn.bgcolor("grey")
    wn.setup(width=600, height=600)
    wn.tracer(0)
    pen = turtle.Turtle()

    while True:
        password = turtle.textinput(title="Password", prompt="Write here your password, it must be 5-characters")
        while len(password) != 5:
            password = turtle.textinput('Password Identifier','Write here your password, the password MUST be 5-characters')
        else: break

    with open('TemporaryFiles/temporarypassword.txt','w') as fp:
        fp.flush
        fp.write(password)


    from subprocess import call
    call(["python", "PasswordIdentifier.py"])

    time.sleep(0.1)

    passworddata = pasworddata2 = ""

    with open('TemporaryFiles/temporarypassworddata.txt') as fp:
        passworddata = fp.read()


    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(-280, 120)
    pen.write(passworddata, font=("Calibri", 20, "bold"))

    time.sleep(5)
    response = turtle.textinput('Password Identifier','Do you want to identify another password? (yes or no): ')
    while response != 'yes' and response != 'no':
        response = turtle.textinput('Password Identifier','Do you want to identify another password? enter "yes" or "no": ')
    if response == 'yes':
        i = 1
        wn.clear()
    elif response == 'no':
        i = 0
    