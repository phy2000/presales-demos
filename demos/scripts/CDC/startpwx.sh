#!/bin/bash
if [ -z "$PWX_HOME" ] ; then
echo PWX_HOME is not set - exiting >&2
exit
fi
$PWX_CMDS/StartListener.sh
$PWX_CMDS/StartLogger.sh
