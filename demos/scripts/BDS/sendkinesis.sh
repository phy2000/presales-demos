#!/bin/bash

USAGE="Usage: $0 <streamname>"

if [ $# -lt 1 ] ; then
	echo $USAGE >&2
	exit -1
fi

TOPIC=$1
SCRIPTDIR=$(cd $(dirname $0) && pwd -P)
PYTHONDIR=$SCRIPTDIR/python

cd $PYTHONDIR
while true; do 
    sleep 10
    DATE=$(date)
    MSG="$TOPIC $DATE"
    echo $MSG >&2
    echo $MSG
done | ./kinesisProducer.py -n $TOPIC
