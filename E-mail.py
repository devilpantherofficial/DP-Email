import smtplib

rocx=smtplib.SMTP('smtp.gmail.com','587')

rocx.ehlo()
rocx.starttls()

email=str(input("Enter Your Gmail : "))
pwd=str(input ("Enter Your Password: "))          
tmail=str(input("Enter Your Target E-Mail : "))
msg=str(input("Enter Your Message: "))
amount=int(input("Enter Your Amount: "))

rocx.login(email,pwd)

for i in range(amount):
   rocx.sendmail(email,tmail,msg)