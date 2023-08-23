import smtplib
from utils import *
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Set up email parameters
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'your_email@gmail.com'
sender_password = 'your_email_password'


# Get borrow date from Borrow table
borrow_id = 1  # replace with actual borrow ID
cnx.execute(f"SELECT Date_borrow FROM Borrow WHERE ID = {borrow_id}")
result = cnx.fetchone()
borrow_date = datetime.strptime(result[0], '%Y-%m-%d')

# Calculate due date and days left
due_date = borrow_date + timedelta(days=10)
days_left = (due_date - datetime.now()).days

# If only 2 days left until due date, send email notification
if days_left == 2:
    # Set up email message
    recipient_email = 'user_email@example.com'  # replace with user's email
    subject = 'Reminder: Your book is due soon!'
    message = f"""\
    Dear User,

    This is a friendly reminder that your borrowed book is due on {due_date}. You have {days_left} days left to return the book to the library.

    If you are unable to return the book by the due date, please contact us to discuss renewal options or any penalties that may apply.

    Thank you for using our library!

    Best regards,
    Library staff
    """

    # Create email object and send it
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print('Email notification sent successfully!')
    except Exception as e:
        print(f'Error sending email: {e}')

# Close database connection
cnx.close()