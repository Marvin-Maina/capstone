import smtplib
from email.mime.text import MIMEText

def send_email():
    sender_email = "marvingitachu@gmail.com"  
    app_password = "bqif rapz nyup sstm" 
    recipient_email = "demomotion50@gmail.com"  

    
    subject = "Motion Detected!"
    body = "Hey! Motion was detected by your camera!"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    send_email()
