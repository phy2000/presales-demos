#!/bin/bash
# 12/7/2017 - removed cdcapp.sh call - the workflow is now  a scheduled application
LOGDIR=/tmp/cdcdemo/$USER/logs
SCRIPTDIR=$(cd $(dirname $0) && pwd -P)
cd $SCRIPTDIR

mkdir -p $LOGDIR
chmod -R 777 /tmp/cdcdemo

# Start monitor process
echo START AT $(date) >> $LOGDIR/monitor.out
nohup $SCRIPTDIR/cdc_monitor.sh 2>&1 >> $LOGDIR/monitor.out &
echo $! >> $LOGDIR/monitor.pid

# Start database changes 
echo START AT $(date) >> $LOGDIR/cdctest.out
nohup $SCRIPTDIR/cdctest.sh $1 2>&1 >> $LOGDIR/cdctest.out &
echo $! >> $LOGDIR/cdctest.pid

tail -f $LOGDIR/*.out
