#!/bin/bash
source /u01/app/infa_shared/presales/set_infa_presales_cloud_Env.sh
cd $INFA_HOME
admind/bin/admin.sh $1
node/bin/node.sh $1 napslxapp01
