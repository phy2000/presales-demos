#!/bin/bash
LOGDIR=/tmp/sparkdemo/logs
SCRIPTDIR=$(cd $(dirname $0) && pwd -P)
cd $SCRIPTDIR

SENDMILLIS=1000
if [ ! -z "$1" ] ; then
    SENDMILLIS=$1
fi

mkdir -p $LOGDIR
chmod 777 -R $LOGDIR

# Start monitor process
echo START AT $(date) >> $LOGDIR/email_monitor.out
nohup $SCRIPTDIR/email_monitor.sh 2>&1 >> $LOGDIR/email_monitor.out &
echo $! >> $LOGDIR/email_monitor.pid

echo START AT $(date) >> $LOGDIR/spark_monitor.out
nohup $SCRIPTDIR/spark_monitor.sh 2>&1 >> $LOGDIR/spark_monitor.out &
echo $! >> $LOGDIR/spark_monitor.pid

# Start database changes 
echo START AT $(date) >> $LOGDIR/sendorders.out
nohup $SCRIPTDIR/sendorders.sh $SENDMILLIS 2>&1 >> $LOGDIR/sendorders.out &
echo $! >> $LOGDIR/sendorders.pid

tail -f $LOGDIR/*.out
