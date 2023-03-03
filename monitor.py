import requests
import smtplib
import os

# The program send request to url, if the page is unavailable or 
# server is unreachable a mail with the error will be sent to
# the providede email address

# Usage instructions: before using the script export the folowing 
# ENV vars: MAIL_ADR, MAIL_PWD.


def send_mail(mail_address, mail_password, send_to, text):

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(mail_address, mail_password)
        smtp.sendmail(mail_address, send_to, text)


def monitor_app(url, send_to):

    MAIL_ADR = os.environ.get('MAIL_ADR')
    MAIL_PWD = os.environ.get('MAIL_PWD')
    
    try:
        response = requests.get(url) 

        if response.status_code == 200:
            print('Website status: ok')
        else:
            print('Website status: FAIL')
            send_mail(MAIL_ADR, MAIL_PWD, send_to, "Subject: SITE BROKEN\n!!PLS HALP!!")

    except Exception as ex:
        message = "Subject: no connection to server\nConnection with app error"
        send_mail(MAIL_ADR, MAIL_PWD, send_to, message)

