#!/usr/bin/env python3
from optparse import OptionParser
from time import sleep
import os
import time
import sys

parser = OptionParser()

parser.usage = "%prog millisecs"

if len(sys.argv) < 2:
    parser.error()
    
pausemilli = int(sys.argv[1])
for data in sys.stdin:
    if data.endswith('\n') :
        print (("%s" % data), end='', flush=True)
    else :
        print("%s" % data, flush=True)
    time.sleep(pausemilli/1000.0)
