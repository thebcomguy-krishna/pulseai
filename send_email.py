import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

def send_briefing(briefing_text):
    # your credentials
    sender_email = "youremail@gmail.com"
    app_password = "your_app_password_here"
    receiver_email = "receiveremail@gmail.com"  # sending to yourself
    
    today = date.today().strftime("%B %d, %Y")
    
    # setup email
    message = MIMEMultipart("alternative")
    message["Subject"] = f"🤖 PulseAI Briefing — {today}"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # plain text version
    text_part = MIMEText(briefing_text, "plain")
    message.attach(text_part)
    
    # send it
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("✅ Briefing sent to your email!")
    
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    # test with dummy text
    test_briefing = "This is a test briefing from PulseAI. If you got this, email works!"
    send_briefing(test_briefing)