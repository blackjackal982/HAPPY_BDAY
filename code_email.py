import smtplib
import sys
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(toaddr):
    fromaddr = "ssirisha639@gmail.com"
    msg = MIMEMultipart()
    msg['Subject'] = "GREETINGS!!!!"
    msg['From'] = fromaddr
    msg['To'] = ",".join(toaddr)


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("ssirisha639@gmail.com", "YOUR PASSWORD")

    body = "WISH YOU A VERY HAPPY BIRTHDAY DEAR!!\nMAY GOD BLESS YOU WITH ABUNDANT LOVE AND HAPPINESS THIS BIRTHDAY\n" \
       "ALL THE BEST FOR YOUR FUTURE ENDEAVOURS.\n" \
       "REGARDS SAI SIRISHA :)"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr,toaddr, text)
    server.quit()

def send_to(cy,date):
    file = open("receiver.txt",'r')
    toaddr = []
    for line in file:
        key,val = line.split(":")
        if str(str(cy)+'-'+key).strip() == str(date).strip():
            if ',' in val:
                toaddr = [i.strip() for i in val.split(",")]
            else:
                toaddr.append(val.strip())
    send_email(toaddr)

def today_time():
    now = datetime.datetime.now()
    today_date = datetime.date.today()  # today's date

    cy = now.year  # current year
    send_to(cy,today_date)

if __name__ == "__main__":
    sys.exit(today_time())
