import smtplib

import config


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESSfrom, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESSfrom, config.EMAIL_ADDRESSto, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Szemetelo"
msg = "Testing periodic mailsending non-docker"

send_email(subject, msg)
