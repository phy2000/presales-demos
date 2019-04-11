#!/bin/bash
source /u01/app/infa_shared/presales/set_infa_presales_cloud_Env.sh
export HOSTNAME=$(/bin/hostname)
cd $INFA_HOME
node/bin/node.sh $1
