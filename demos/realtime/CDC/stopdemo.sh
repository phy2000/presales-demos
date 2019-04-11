#!/bin/bash
# 12/7/2017 - removed stop of cdcapp.sh

LOGDIR=/tmp/cdcdemo/$USER/logs
SCRIPTDIR=$(cd $(dirname $0) && pwd -P)
cd $SCRIPTDIR

# STOP database changes 
echo stopping cdctest
echo STOP AT $(date) >> $LOGDIR/cdctest.out
kill $(tail -1 $LOGDIR/cdctest.pid)
sleep 2
kill -9 $(tail -1 $LOGDIR/cdctest.pid) 2>/dev/null

# STOP monitor process
echo stopping cdcmonitor
echo STOP AT $(date) >> $LOGDIR/monitor.out
kill $(tail -1 $LOGDIR/monitor.pid)
sleep 2
kill -9 $(tail -1 $LOGDIR/monitor.pid) 2>/dev/null

