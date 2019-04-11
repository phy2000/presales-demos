#!/usr/bin/env python3
from optparse import OptionParser
from kafka import KafkaConsumer
from time import time
from os import walk
import signal 
import sys
import os

def signal_handler(signal, frame):
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

parser = OptionParser()

parser.usage = "%prog -t TOPIC [-b HOST:PORT] "
parser.add_option("-t", 
    dest="topicname", help="kafka topic to listen", metavar="TOPIC", default="none")
parser.add_option("-b",
    dest="broker", help="kafka broker in <host>:<port> format", metavar="BROKER", default="none")
parser.add_option("-B",
    dest="fromBeginning", help="Read queue contents from beginning", metavar="FROMBEGINNING", action="store_true", default=False)

(options, args) = parser.parse_args()

if options.broker == "none" :
    options.broker="localhost:9092"

if options.topicname == "none" :
   parser.print_help()
   sys.exit(1)

if options.topicname == "none" :
   parser.print_help()
   sys.exit(1)
print("topic=%s; broker=%s" % (options.topicname, options.broker), file=sys.stderr)

topic=options.topicname
broker=options.broker

if options.fromBeginning :
    offset_reset='smallest'
else :
    offset_reset='largest'

consumer = KafkaConsumer(topic,bootstrap_servers=broker, auto_offset_reset=offset_reset)

for message in consumer:
    #data =  message.value.decode('utf8')
    data =  message.value
    if False:
        if data.endswith('\n') :
            print (("%s" % data), end='', flush=True)
        else :
            print ("%s" % data, flush=True)
    print ("%s" % data, flush=True)
