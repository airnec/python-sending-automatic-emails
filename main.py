import my_password
import random
import datetime as dt
import smtplib
from email.mime.text import MIMEText

# PICKING THE DAY
# ------------------------------------------------------------------------
now = dt.datetime.now()
day = now.weekday()
hour = now.hour
minute = now.minute

if day == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # SENDING EMAIL
    # ------------------------------------------------------------------------
    # Email Configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # For TLS
    email_address = "pythondevelopertester@gmail.com"
    email_password = my_password.my_password  # Use app password if 2FA is enabled
    recipient = "example@example.com"

    # Create Email
    subject = "Weekly Motivational Quote"
    body = quote
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = email_address
    message["To"] = recipient

    try:
        # Connect to SMTP Server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade to secure connection
        server.login(email_address, email_password)
        server.send_message(message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()
