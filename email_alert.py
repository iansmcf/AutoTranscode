#!/usr/local/bin/python3.6
import subprocess
from os import devnull

def email_alert(recipient, from_name, subject, message):
    subprocess.run("echo \"" + message + "\" | mail -s \"" + subject + "\" " + recipient,
    shell=True)
    return
