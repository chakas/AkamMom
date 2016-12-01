# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


# Create a text/plain message


# Send the message via our own SMTP server, but don't include the
# envelope header.
server = smtplib.SMTP('labsmtp.akamai.com')
def sendemail(body):

    msg = MIMEText(body,'html')

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = "MOM"
    msg['From'] = "vt@akamai.com"
    msg['CC'] = "prathore@akamai.com"
    msg['To'] = "nmurthy@akamai.com"
    server.sendmail("vt@akamai.com", ["nmurthy@akamai.com","prathore@akamai.com"], msg.as_string())

    print "done"


