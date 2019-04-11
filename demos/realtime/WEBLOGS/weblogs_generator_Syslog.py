#!/usr/bin/env python
"""
@file    weblogs_generator.py
@author  Massimiliano Ciccone
@date    27-06-2017
@version 1
"""

import syslog_client
import sys, subprocess, random
from datetime import datetime
import time
from collections import defaultdict
import math

def main(args=None):
	c = raw_input("Type something to start simulation...")
	#dttm_str=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
	#newline=dttm_str+" "+"6914 28.154.143.132(-83.0597,42.511293) (rueg@gmail.com)(2012-11-07)[Google Chrome v42.0 WIN x64 8.1] (suprt)acme.com[main:return] 17(W) 30 20150116194725-20150108180106 Java:YES,Paid=NO "http://www.acme.com/returns?product_id=70407;reason=Product not satisfactory"(15)0 [alang=en-us,cookies=YES]2457039"
	#print(newline)
	#log = syslog_client.Syslog("localhost")
	#log.send("newline", syslog_client.WARNING)
	#log.warn(newline)
	#c = raw_input("Type something to CONTINUE syslog simulation...")
	#read the weblogs file line by line and replace the timestamp with a fresh one.
	with open('weblogs.log') as fp:
		for line in fp:
			print (line)
			# Split the weblog line up to first occurrence of space (to remove timestamp)
			lineList=line.split(" ", 1)
			dttm_str=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
			newline=dttm_str+" "+lineList[1]
			print(newline)
			log = syslog_client.Syslog("localhost")
			#log.send("newline", syslog_client.WARNING)
			log.warn(newline)
			c = raw_input("Type something to CONTINUE syslog simulation...")
	print(">> Simulation closed")
	sys.stdout.flush()

if __name__ == "__main__":
    main()
