#!/bin/bash 

SCRIPTDIR=$(cd $(dirname $0) && pwd)

NAMELIST=$SCRIPTDIR/usernames.txt
if [ ! -z "$1" ] ; then
NAMELIST=$1
fi

if [ ! -r $NAMELIST ] ; then
    echo file "$NAMELIST not found!" >&2
    exit -1
fi

cd $SCRIPTDIR
for name in $(<$NAMELIST) ; do
    echo $name 
    aws kinesis delete-stream  --stream-name stream_$name
    sleep 1
done

