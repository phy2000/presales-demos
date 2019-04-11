#!/usr/bin/env python3
from optparse import OptionParser
from kafka import KafkaProducer
from time import sleep
from os import walk
import os
import time
import sys

parser = OptionParser()

parser.usage = "%prog -t TOPIC [-b HOST:PORT] "

parser.add_option("-t",
    dest="topicname", help="kafka topic to send", metavar="TOPIC", default="none")
parser.add_option("-b",
    dest="broker", help="kafka broker in <host>:<port> format", metavar="BROKER", default="none")
(options, args) = parser.parse_args()

if options.topicname == "none" :
   parser.print_help()
   sys.exit(1)

if options.broker == "none" :
    options.broker = "localhost:9092"

topic=options.topicname
broker=options.broker

print("topic=%s; broker=%s" % (options.topicname, options.broker), file=sys.stderr)

producer = KafkaProducer(bootstrap_servers=broker)

for content in sys.stdin:
    producer.send(topic, content.encode('utf8'))

print("EOF - please wait...")
time.sleep(5)
