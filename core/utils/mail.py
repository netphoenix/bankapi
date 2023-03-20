import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(to: str, subject: str, message: str, file: bytes = None) -> None:
    msg = MIMEMultipart()
    msg['From'] = 'netphoenix@yandex.com'
    msg['To'] = to
    msg.attach(MIMEText(message))
    if file:
        part = MIMEApplication(file, Name='img.jpeg')
        part['Content-Disposition'] = 'attachment; filename="img.png"'
        msg.attach(part)

    context = ssl.create_default_context()
    #server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    server = smtplib.SMTP('smtp.yandex.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('netphoenix@yandex.com','ztaxhwtlxzznxodp')
    server.sendmail('netphoenix@yandex.com', to, msg.as_string())
