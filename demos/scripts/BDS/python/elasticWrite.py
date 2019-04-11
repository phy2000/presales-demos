#!/usr/bin/env python3
from optparse import OptionParser
import os
import time
import sys
import json
import datetime
from elasticsearch import Elasticsearch


parser = OptionParser()

parser.usage = "%prog -i INDEX -e ELASTICSERVER -d DOC_TYPE [-v]"

parser.add_option("-i",
    dest="index", help="Elasticsearch index to write", metavar="INDEX", default="none")
parser.add_option("-e",
    dest="elasticserver", help="Elasticsearch server in <host>:<port> format", metavar="ELASTICSERVER", default="none")
parser.add_option("-t",
    dest="doc_type", help="Document type for index", metavar="DOC_TYPE", default="none")
parser.add_option("-v",
    dest="verbose", action="store_true", help="verbosity", metavar="VERBOSITY", default=False)

(options, args) = parser.parse_args()

if options.index == "none" :
   parser.print_help()
   sys.exit(1)

if options.elasticserver == "none" :
    options.elasticserver = "localhost:9200"

index=options.index
elasticserver=options.elasticserver
doc_type=options.doc_type
verbose = options.verbose

print("index=%s; elasticserver=%s; doc_type=%s" % (index, elasticserver, doc_type), file=sys.stderr)

es = Elasticsearch()

for content in sys.stdin:
    jContent = json.loads(content)
    jContent["post_date"] = datetime.datetime.utcnow().isoformat('T');
    content = json.dumps(jContent)
    res = es.index(index=index, doc_type=doc_type, body=content)
    if verbose:
        print("%s" % content)
        print(res['created'])

print("EOF - please wait...", file=sys.stderr)
time.sleep(5)
