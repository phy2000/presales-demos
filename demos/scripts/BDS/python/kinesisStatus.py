#!/usr/bin/env python3
from optparse import OptionParser
from kafka import KafkaProducer
from time import sleep
import os
import time
import sys
import json
import boto3

from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

creds = {}
exec(open("cred.py").read(), creds)
aws_access_key = creds["aws_access_key"]
aws_secret_key = creds["aws_secret_key"]

client = boto3.client(
        'kinesis',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name="us-west-2"
    )

parser = OptionParser()

parser.usage = "%prog -n streamname "

parser.add_option("-n",
    dest="streamname", help="stream name to send to", metavar="STREAMNAME", default="none")
(options, args) = parser.parse_args()

if options.streamname == "none" :
   parser.print_help()
   sys.exit(1)

streamname=options.streamname

print("streamname=%s; " % (options.streamname))

response = client.describe_stream(StreamName=streamname, Limit=1)

for key, value in response.items():
    print("=========================\n" + key)
    print("%s" % json.dumps(value, default=json_serial, indent=4))
    

# time.sleep(5)
