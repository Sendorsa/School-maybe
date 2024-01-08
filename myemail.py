import smtplib
from email.mime.text import MIMEText
import funt
global x


def otp_check(ee):
    a=send_mail(ee)
    b=int(input("Enter OTP "))
    if b==a:
        print("Access granted")
    else:
        print("L bro")
        
def send_mail(w):
    gmail_user = "otptest256@gmail.com"  # Your Gmail credentials
    gmail_app_password = "auud oatl kwzx gvbv"  # Use the App Password generated for your account
    to_email = w
    
    # Subject and body of the email
    subject = "OTP"
    funt.otp()
    x=funt.otp()
    body = f"OTP:{x}"
    
    # Create the MIMEText object
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = gmail_user
    message["To"] = to_email
    
    # Connect to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        # Login to your Gmail account using the App Password
        server.login(gmail_user, gmail_app_password)
        
        # Send the email
        server.sendmail(gmail_user, to_email, message.as_string())
    
    print("Email sent successfully!")
    return x