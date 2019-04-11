#!/bin/bash 

USAGE="Usage: $0 <kafkatopic>"

if [ $# -lt 1 ] ; then
	echo $USAGE >&2
	exit -1
fi

TOPIC=$1

THISDIR=$(cd $(dirname $0) && pwd)
PYTHONDIR=$THISDIR/python
cd $PYTHONDIR

DATADIR=$THISDIR/data/mlb-tweets

./replayKafka.py -b localhost:9092 -d $DATADIR -t $TOPIC
