#!/bin/bash

if ! /var/scripts/iis/checkInfaUser ; then
    exit 1
fi
HDFS_SRC_DIR=/user/infa/iis/cdc_stage
HDFS_TGT_DIR=/user/infa/iis/cdc_finish
# ssh -n infa@napslxcdh01 hadoop fs -mv ${HDFS_SRC_DIR}/* $HDFS_TGT_DIR
hadoop fs -mv ${HDFS_SRC_DIR}/* $HDFS_TGT_DIR
