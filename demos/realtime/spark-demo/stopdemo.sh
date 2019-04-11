#!/bin/bash

LOGDIR=/tmp/sparkdemo/logs
SCRIPTDIR=$(cd $(dirname $0) && pwd -P)
cd $SCRIPTDIR

# STOP database changes 
echo stopping sendorders
echo STOP AT $(date) >> $LOGDIR/sendorders.out
kill $(tail -1 $LOGDIR/sendorders.pid)
sleep 2
kill -9 $(tail -1 $LOGDIR/sendorders.pid) 2>/dev/null

# STOP email_monitor process
echo stopping email_monitor
echo STOP AT $(date) >> $LOGDIR/email_monitor.out
kill $(tail -1 $LOGDIR/email_monitor.pid)
sleep 2
kill -9 $(tail -1 $LOGDIR/email_monitor.pid) 2>/dev/null

# STOP sparkmonitor process
echo stopping spark_monitor
echo STOP AT $(date) >> $LOGDIR/spark_monitor.out
kill $(tail -1 $LOGDIR/spark_monitor.pid)
sleep 2
kill -9 $(tail -1 $LOGDIR/spark_monitor.pid) 2>/dev/null

