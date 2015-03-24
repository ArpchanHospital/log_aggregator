import sys
from EmailBuilder import EmailBuilder
from ReadConfig import Config
from Utils import get_current_timestamp
from ZipLogFiles import ZipLogFiles


def controller():
    username = sys.argv[1]
    password = sys.argv[2]
    email_from = sys.argv[3]
    email_to = sys.argv[4]
    archive_name = ZipLogFiles(Config("config.json").config).archive_name
    EmailBuilder(username, password, email_from, email_to) \
        .add_attachment(archive_name, archive_name).add_subject("Log Files " + get_current_timestamp()).add_body(
        "Logs as of date - " + get_current_timestamp()).send_email()


if __name__ == "__main__":
    controller()