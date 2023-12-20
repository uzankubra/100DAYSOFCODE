# smtp: simple mail transfer protocol(sender-> recipient)


import smtplib
import datetime as dt
import random

MY_EMAIL="protocoltestmail2@gmail.com"
PASSWORD="km2002()"

now=dt.datetime.now()
weekday=now.weekday()
if weekday==1:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(MY_EMAIL,PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL, to_addrs="kubraauzann@gmail.com", msg=f"HI KUBRA YOU ARE AWESOME")
        connection.close()






