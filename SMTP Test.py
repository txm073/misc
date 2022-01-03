import smtplib
from email.message import EmailMessage
import imghdr
import os

os.chdir(os.path.dirname(__file__))

contacts = {
            "Jason":"jmiles17@patchamhigh.org.uk",
            "Joe":"jsnelling17@patchamhigh.org.uk",
            "Tom":"tomtombarnes2@gmail.com",
            "Lisa":"ljhmillar@gmail.com",
            "Peter":"peterbarneslondon@gmail.com",
            "Jill":"jillwhiteleyb@gmail.com"
            }

def add_attachment(msg,file):
    with open(file,"rb") as f:
        file_contents = f.read()
        file_name = f.name
        file_type = imghdr.what(file_name)
        msg.add_attachment(file_contents, filename=file_name, maintype="image", subtype=file_type)

def test_email():
    msg = EmailMessage()
    msg["Subject"] = "Test"
    msg["From"] = "SMTPTestAddress864@gmail.com"
    msg["To"] = contacts["Tom"]
    msg.set_content("This is a test email sent using Python!")
    add_attachment(msg, "test_image.jpg")

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp: 
        smtp.login("SMTPTestAddress864@gmail.com","qdh5ykmtDrpj")
        input("Press enter to send: ")
        smtp.send_message(msg)
        print("Message sent")