from urllib3 import Retry
import time

password = password2 = ""

with open('TemporaryFiles/temporarypassword.txt') as fp:
    password = fp.read()



A1 = ""
B1 = ""
B2 = ""
B3 = ""
C1 = ""


#checking for numbers in the password

if (any(chr.isdigit() for chr in password)):
    A1 = "There are numbers in your password\n"
else:
    A1 = "There are no numbers in your password\n"



#checking for letters in the password

TrueLetters = (any(chr.isalpha() for chr in password))
TrueUpper = (any(chr.isupper() for chr in password))
TrueLower = (any(chr.islower() for chr in password))

if TrueLetters:
    B1 = "There are letters in your password:\n"
    if TrueUpper:
        B2 = "# - There are upper letters in your password\n"
    else:
        B2 = "# - There are no upper letters in your password\n"
    
    if TrueLower:
        B3 = "# - There are lower letters in your password\n"
    else:
        B3 = "# - There are no lower letters in your password\n"


else:
    B1 = "There are no letters in your password"
    B2 = ""
    B3 = ""



with open('TemporaryFiles/temporarypassworddata.txt','w') as fp:
    fp.flush
    fp.write(A1)
    fp.write(B1)
    fp.write(C1)
    fp.write(B2)
    fp.write(B3)