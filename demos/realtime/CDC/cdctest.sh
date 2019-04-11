#!/bin/bash
    i=0;
    while [ $i -lt ${1:-100} ]; do
        echo -n $i.
        let i=i+1;
        let j=2*i;
        ts=`date "+%d-%b-%Y %r"`;
        mykey="$ts-$i";
        echo "insert into cdctest ( keystring, count, tstamp, numfield, vcharfield) values ('$mykey', $i,  '$ts',$i,'$i'); " | sqlplus cdctest/cdctest@XE > /dev/null
        ( sleep 4;
        echo "update cdctest set numfield = '$j', tstamp = '`date "+%d-%b-%Y %r"`' where keystring = '$mykey'; " | sqlplus cdctest/cdctest@xe ) > /dev/null & sleep 1;
        modulo=$(expr $i % 3)
        if [ $modulo -ne 0 ] ; then
            ( sleep 10;
              echo "delete from cdctest where keystring = '$mykey'; " | sqlplus cdctest/cdctest@XE ) > /dev/null & sleep 1;
            fi
    done
    echo
    echo $0 Finish at $(date)
