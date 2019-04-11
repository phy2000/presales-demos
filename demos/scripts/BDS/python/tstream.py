#!/usr/bin/env python3
# Import the necessary package to process data in JSON format

try:
    import sys
    import json
except ImportError:
    import simplejson as json

from optparse import OptionParser
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


parser = OptionParser()
parser.usage = "%prog [-f SEARCHPATTERN]"
parser.add_option("-f", 
    dest="filter", help="search pattern to filter input", metavar="SEARCHPATTERN", default="none")
(options, args) = parser.parse_args()
filter = options.filter

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
creds = {}
exec(open("cred.py").read(), creds)
oauth = OAuth(creds["access_key"], creds["access_secret"], creds["consumer_key"], creds["consumer_secret"])

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
if filter == "none" :
    print("sampling twitter stream", file=sys.stderr)
    iterator = twitter_stream.statuses.sample()
else :
    #iterator = twitter_stream.statuses.filter(track="@strataconf,@zoomdata,#stratadata,@informatica,@theiot")
    print("filter twitter stream", file=sys.stderr)
    iterator = twitter_stream.statuses.filter(track=filter)

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print("%s" % json.dumps(tweet))
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 
