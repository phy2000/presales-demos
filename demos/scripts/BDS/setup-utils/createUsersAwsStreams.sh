#!/bin/bash 

SCRIPTDIR=$(cd $(dirname $0) && pwd)
NAMELIST=$SCRIPTDIR/usernames.txt

if [ ! -z $1 ] ; then
NAMELIST=$1
fi

if [ ! -r $NAMELIST ] ; then
    echo file "$NAMELIST not found!" >&2
    exit -1
fi

cd $SCRIPTDIR
for name in $(<$NAMELIST) ; do
    echo -n $name... 
    while ! aws kinesis create-stream --shard-count 1 --stream-name stream_$name
    do
	echo WAITING...
	sleep 20
    done
    echo $name OK
    sleep 1
done

