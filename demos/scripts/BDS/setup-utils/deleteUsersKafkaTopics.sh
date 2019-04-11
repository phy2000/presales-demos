#!/bin/bash 

SCRIPTDIR=$(cd $(dirname $0) && pwd)
NAMELIST=$SCRIPTDIR/usernames.txt

if [ ! -z "$1" ] ; then
NAMELIST=$1
fi

if [ -z "$KAFKA_HOME" ] ; then
    KAFKA_HOME=/home/ec2-user/kafka/kafka_2.11-0.10.1.1
fi

if [ ! -r $NAMELIST ] ; then
    echo file "$NAMELIST not found!" >&2
    exit -1
fi

cd $SCRIPTDIR
for name in $(<$NAMELIST) ; do
    echo $name
    $KAFKA_HOME/bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic source-$name
    $KAFKA_HOME/bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic target-$name
done

