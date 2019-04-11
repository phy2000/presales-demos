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

parser.usage = "%prog [ -b HOST:PORT] "
parser.add_option("-b",
    dest="broker", help="kafka broker in <host>:<port> format", metavar="BROKER", default="none")

(options, args) = parser.parse_args()

if options.broker == "none" :
    options.broker="localhost:9092"

print("broker=%s" % (options.broker), file=sys.stderr)

broker=options.broker

consumer = KafkaConsumer(bootstrap_servers=broker)

for listtopic in consumer.topics():
    print("%s" % (listtopic))
