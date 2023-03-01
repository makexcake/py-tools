import requests
import smtplib
import os

def send_mail(mail_address, mail_password, send_to, text):

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(mail_address, mail_password)
        smtp.sendmail(mail_address, send_to, text)


def monitor_website(url, send_to):

    EMAIL_ADRESS = os.environ.get('MAIL_ADD')
    EMAIL_PASSWORD = os.environ.get('MAIL_PWD')
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print('Website status: ok')
        else:
            print('Website status: FAIL')
            # send mail to myself
            send_mail(EMAIL_ADRESS, EMAIL_PASSWORD, send_to, "Subject: SITE BROKEN\n!!PLS HALP!!")

    except Exception as ex:
        print(f'Connection ERROR happened: {ex}')
        message = "Subject: no connection to server\nConnection with app error: " + str(ex)
        send_mail(EMAIL_ADRESS, EMAIL_PASSWORD, send_to, message)



monitor_website("https://gomomgle.com/skdlk", 'v.nudelman@gmail.com')