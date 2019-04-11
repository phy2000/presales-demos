#!/bin/bash
PWX_BASE=/opt/infa/PWX
source $PWX_BASE/pwx_env.sh
cd $PWX_BASE
case $1 in
start)
	./start_pwx.sh
	sleep 5
	./start_pub.sh
	;;

stop)
	./stop_pub.sh
	sleep 5
	./stop_pwx.sh
	;;

*)
	echo $USAGE >&2
	;;
esac
