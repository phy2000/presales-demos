#!/usr/bin/env python3
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from optparse import OptionParser

import sys

parser = OptionParser()
parser.usage = "%prog [-f SEARCHPATTERN]"
parser.add_option("-f", 
    dest="filter", help="search pattern to filter input", metavar="SEARCHPATTERN", default="none")
(options, args) = parser.parse_args()
if options.filter  == "none" :
   parser.print_help()
   sys.exit(1)

filter = options.filter

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
creds = {}
exec(open("cred.py").read(), creds)
oauth = OAuth(creds["access_key"], creds["access_secret"], creds["consumer_key"], creds["consumer_secret"])

# Initiate the connection to Twitter Streaming API
twitter = Twitter(auth=oauth)

# Get a sample of the public data following through Twitter
tweet_count = 10
query = twitter.search.tweets(q=filter, result_type='recent', lang='en', count=tweet_count)

# Print each tweet in the stream to the screen 
for result in query["statuses"]:
	print(json.dumps(result))
