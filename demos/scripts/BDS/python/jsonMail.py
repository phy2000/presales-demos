#!/usr/bin/env python3
from optparse import OptionParser
from time import sleep
import os
import time
import sys
import json
import smtplib
from email.mime.text import MIMEText

parser = OptionParser()

parser.usage = "%prog"

for data in sys.stdin:
    mailobj = json.loads(data);
    outmsg = MIMEText(mailobj["body"]);
    outmsg['Subject'] = mailobj["subject"];
    outmsg['From'] = mailobj["from"];
    outmsg['To'] = mailobj["to"];
    s = smtplib.SMTP('localhost');
    s.send_message(outmsg);
    s.quit()
