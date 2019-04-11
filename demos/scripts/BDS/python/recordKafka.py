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

parser.usage = "%prog -t TOPIC -d DIR-TO-SAVE -b HOST:PORT [-v] "
parser.add_option("-t", 
    dest="topicname", help="kafka topic to listen", metavar="TOPIC", default="none")
parser.add_option("-d", 
    dest="dir", help="(empty) destination directory to save messages", metavar="DIR", default="none")
parser.add_option("-b",
    dest="broker", help="kafka broker in <host>:<port> format", metavar="BROKER", default="none")
parser.add_option("-v",
    dest="verbose", action="store_true", help="verbosity", metavar="BROKER", default=False)

(options, args) = parser.parse_args()

if options.topicname == "none" or options.dir == "none" or options.broker == "none":
   parser.print_help()
   sys.exit(1)

print("topic=%s; dir=%s; broker=%s" % (options.topicname, options.dir, options.broker))

start=-1
topic=options.topicname
path=options.dir+'/'
broker=options.broker
verbose=options.verbose

if not os.path.isdir(options.dir):
   print("Error - %s does not exist or is not a directory" % options.dir)
   sys.exit(1)

consumer = KafkaConsumer(topic,bootstrap_servers=broker)
for message in consumer:
    # Start offset 0 on first message
    if start < 0:        
        start=time()
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    usec=int((time()-start)*1000000)
    if verbose:
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    filename=path+str(usec).zfill(13)+'.msgdata'
    with open(filename,'wb') as f:
        if verbose:
            print('Store message in '+filename)
        f.write(message.value)
