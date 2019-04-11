#!/bin/bash
# Check VDS and start after change

    ( echo updateVDS on `date +%Y%m%d-%H%M%S`;
    thisIp=`ifconfig eth0 | egrep inet | grep -v inet6| awk '{print $2}'`;
    oldIp=`perl -ne 'print $1 if /networkInterface=(.*)/' $INFA_HOME/node/config/node.cnf`;
    thisIp=`ifconfig eth0 | egrep inet | grep -v inet6| awk '{print $2}'`;
    oldIp=`perl -ne 'print $1 if /networkInterface=(.*)/' $INFA_HOME/node/config/node.cnf`;
    if [ $thisIp == $oldIp ]; then
        echo "Nothing to do";
    else
        echo "thisIp != oldIp";
        for i in $INFA_HOME/admind/config/umestored.cfg $INFA_HOME/admind/config/lbmrd.xml $INFA_HOME/admind/config/admind.cnf $INFA_HOME/node/config/node.cnf;
        do
            perl -p -i.`date +%Y%m%d-%H%M%S` -e 's/'$oldIp'/'$thisIp'/g' $i;
            ls --color=auto -ls $i*;
        done;
    fi ) | tee -a $INFA_HOME/updateVDS.log
