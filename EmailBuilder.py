import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


class EmailBuilder:
    def __init__(self, username, password, email_from, email_to):
        self.email = MIMEMultipart()
        self.email["From"] = email_from
        self.email["To"] = email_to
        self.server = smtplib.SMTP("smtp.gmail.com:587")
        self.server.ehlo()
        self.server.starttls()
        self.server.login(username, password)

    def add_attachment(self, file_path, file_name):
        ctype, encoding = mimetypes.guess_type(file_path)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        fp = open(file_path, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=file_name)
        self.email.attach(attachment)
        return self

    def add_subject(self, subject):
        self.email["Subject"] = subject
        return self

    def add_body(self, body):
        self.email.attach(MIMEText(body, 'plain'))
        return self

    def send_email(self):
        self.server.sendmail(self.email['From'], self.email['To'], self.email.as_string())
        self.server.quit()