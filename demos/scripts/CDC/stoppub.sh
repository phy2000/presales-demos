#!/bin/bash
if [ -z "$PWXPUB_HOME" ] ; then
echo PWXPUB_HOME is not set - exiting >&2
exit
fi
$PWXPUB_CMDS/StopPublisher.sh
