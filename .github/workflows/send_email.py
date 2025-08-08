import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_gmail_notification():
    """
    Sends an email notification using Gmail's SMTP server.
    Reads configuration from environment variables set in the GitHub workflow.
    """
    # --- Configuration from environment variables ---
    sender_email = os.environ.get("GMAIL_USERNAME")
    app_password = os.environ.get("GMAIL_PASSWORD")
    recipient_email = os.environ.get("RECIPIENT_EMAIL")
    subject = os.environ.get("EMAIL_SUBJECT")
    body = os.environ.get("EMAIL_BODY")

    # --- Validate that all required variables are present ---
    if not all([sender_email, app_password, recipient_email, subject, body]):
        print("Error: One or more required email environment variables are not set.", file=sys.stderr)
        sys.exit(1)

    # --- Create the email message ---
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # --- Send the email using a secure connection ---
    try:
        print(f"Connecting to Gmail SMTP to send email to {recipient_email}...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    send_gmail_notification()

