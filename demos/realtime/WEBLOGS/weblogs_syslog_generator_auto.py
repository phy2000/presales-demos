#!/usr/bin/env python
"""
@file    weblogs_generator.py
@author  Massimiliano Ciccone
@date    27-06-2017
@version 1
"""
#shuf file.txt -o shuffled_lines_file.txt

import syslog_client
import sys
from datetime import datetime
import time
from collections import defaultdict
import math
from random import randint

def main(args=None):
	t_step=1  # avg time step length
	#max_logs=600 #Stop feeding after n weblogs
	max_logs=1800 #Stop feeding after n weblogs
	logs_count=0 
	#c = raw_input("Press ENTER to start WEBLOGS simulation...")
	#read the weblogs file line by line and replace the timestamp with a fresh one.
	log = syslog_client.Syslog(host="localhost",port=8514)
	with open('weblogs.log') as fp:
		for line in fp:
			print (line)
			# Split the weblog line up to first occurrence of space (to remove timestamp)
			lineList=line.split(" ", 1)
			dttm_str=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
			newline=dttm_str+" "+lineList[1]
			print(newline)
			#log.send("newline", syslog_client.WARNING)
			log.warn(newline)
    			#my_t_step=randint(1,2*t_step)       # random time steps
			time.sleep(1)
			logs_count=logs_count+1
			if (logs_count==max_logs):
				print(">> %d weblogs have been sent"% (max_logs))
				break
	print(">> Simulation closed")
	sys.stdout.flush()

if __name__ == "__main__":
    main()
