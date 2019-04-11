#!/usr/bin/env python3
from optparse import OptionParser
from time import sleep
from os import walk
import os
import time
import sys

parser = OptionParser()

parser.usage = "%prog -d DIR-TO-READ [-w SECS] [-l SECS] [-v] "

parser.add_option("-d",
    dest="dir", help="source directory for saved messages", metavar="DIR", default="none")
parser.add_option("-w",
    dest="wait", type="int", help="Wait seconds before sending (5)", metavar="WAIT", default=5)
parser.add_option("-l",
    dest="linger", type="int", help="linger seconds after sending (5)", metavar="LINGER", default=5)
parser.add_option("-v",
    dest="verbose", action="store_true", help="verbosity", metavar="VERBOSITY", default=False)

(options, args) = parser.parse_args()

if options.dir == "none" :
   parser.print_help()
   sys.exit(1)

print("dir=%s; wait=%d" % (options.dir , options.wait), file=sys.stderr)


path=options.dir+'/'
waittime=options.wait
linger=options.linger
verbose=options.verbose

if not os.path.isdir(options.dir):
   print("Error - %s does not exist or is not a directory" % options.dir)
   sys.exit(1)

files = []

if waittime > 0:
    time.sleep(waittime)

for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)

lastTime=0
sortedFiles=sorted(files)
for f in sortedFiles:
    if '.msgdata' in f:
        thisFile=f
        usec=int(f.replace('.msgdata',''))

        sleepTime=usec/1000000.-lastTime

        if verbose:
            print('Will send '+f+' in '+str(sleepTime)+' sec to topic '+topic, file=sys.stderr)
        with open(path+f,'rb') as file:
            content=file.read()
            sleep(sleepTime)
            print("%s" % content.decode('utf8'))
        lastTime=usec/1000000.
    else:
        continue

time.sleep(linger)
