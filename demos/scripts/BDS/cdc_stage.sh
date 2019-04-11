#!/bin/bash

if ! /var/scripts/iis/checkInfaUser ; then
    exit 1
fi
HDFS_SRC_DIR=/user/infa/iis/cdc_land
HDFS_TGT_DIR=/user/infa/iis/cdc_stage
TIME_LIMIT=120
NOW=$(date +%s)
count=0
while read mode repl user group size mdate mtime fpath ; do
    CREATE_TIME=$(date --date="$mdate $mtime" +%s)
    ((AGE=$NOW-$CREATE_TIME))
    if [ $AGE -le $TIME_LIMIT ]; then break; fi
    echo "NOW=$NOW; CREATE_TIME=$CREATE_TIME; $fpath is $AGE seconds old"
    # ssh -n infa@quickstart hadoop fs -mv $fpath $HDFS_TGT_DIR
    hadoop fs -mv $fpath $HDFS_TGT_DIR
    ((count++))
#done < <(ssh infa@napslxcdh01 hadoop fs -ls -r -t $HDFS_SRC_DIR | tail -n +2 )
done < <(hadoop fs -ls -r -t $HDFS_SRC_DIR | tail -n +2 )
echo processed $count files
if [ "$count" -gt 0 ] ; then
    exit 0
else
    exit 1
fi
