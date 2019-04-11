#!/bin/bash

USAGE="$0 <pause in milliseconds>"

SCRIPTDIR=$(cd $(dirname $0) && pwd -P)

if [ $# -lt 1 ] ; then
    echo $USAGE >&2
    exit -1
fi

PAUSEMILLI=$1
echo $0: Send Start $(date)
tail -n +2 data/orders-by-date.csv | pause $PAUSEMILLI | kafkaProducer hermes_orders 
echo $0: Send Stop $(date)
