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
    dest="streamname", help="stream name to read from", metavar="STREAMNAME", default="none")
(options, args) = parser.parse_args()

if options.streamname == "none" :
   parser.print_help()
   sys.exit(1)

streamname=options.streamname

print("streamname=%s; " % (streamname))

response = client.describe_stream(StreamName=streamname, Limit=1)
shardId = response['StreamDescription']['Shards'][0]['ShardId']
shard_iterator = client.get_shard_iterator(StreamName=streamname,
        ShardId=shardId,
        ShardIteratorType='LATEST')

my_shard_iterator = shard_iterator['ShardIterator']
record_response = client.get_records(ShardIterator=my_shard_iterator, Limit=1)

count = 1
while 'NextShardIterator' in record_response:
    if len(record_response['Records']) > 0 :
        for data_record in record_response['Records'] :
            current_data = (data_record['Data'].decode('utf8'))
            if current_data.endswith('\n') :
                print ("%s" % (current_data), end='')
            else :
                print ("%s" % (current_data))
            count += 1
    else :
        time.sleep(1)
    try:
        record_response = client.get_records(ShardIterator=record_response['NextShardIterator'], Limit=1000)
    except:
        print("exception", file=sys.stderr)
        time.sleep(2)
