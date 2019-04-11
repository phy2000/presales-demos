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

response = client.list_streams(Limit=100)

while True:
    for name in response['StreamNames'] :
        print("%s" % name)
    if response['HasMoreStreams']:
        response = client.list_streams(Limit=100, ExclusiveStartStreamName=name)
    else :
        break
    

# time.sleep(5)
