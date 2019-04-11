#!/bin/bash

SCRIPTDIR=$(cd $(dirname $0); pwd -P)
cd $SCRIPTDIR

if ! /var/scripts/iis/checkInfaUser ; then
    exit 1
fi

DOMAIN_NAME=infa_presales_cloud
DIS_NAME=presales_dis
WF_NAME=wf_CDC_Demo
APP_NAME=App_wf_CDC_Demo
USERNAME=Administrator
PASSWORD=Administrator
LOOPTIME=120

while true; do
    start=$(date +%s)
    ((next=$start+$LOOPTIME))
    echo start at $(date)
    /opt/infa/PLATFORM/server/bin/infacmd.sh wfs startWorkflow -dn $DOMAIN_NAME -sn $DIS_NAME -un $USERNAME -pd $PASSWORD -wf $WF_NAME -a $APP_NAME
    echo finish at $(date)
    finish=$(date +%s)
    ((sleeptime=$next-$finish))
    sleep $sleeptime
done
