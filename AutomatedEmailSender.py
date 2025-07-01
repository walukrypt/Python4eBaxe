import smtplib
from email.mime.text import MIMEText

def send_email(sender, password, receiver, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

# Example: send_email("you@gmail.com", "your_app_password", "friend@gmail.com", "Hey!", "Check this out.")
