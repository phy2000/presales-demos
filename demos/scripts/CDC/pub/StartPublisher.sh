echo '>>>>>>>>>>>>>>>>>>>' $(date) >> Publisher.out
nohup $PWXPUB_HOME/bin/PwxCDCPublisher.sh instance=ora_demo restart=FROM_END >> Publisher.out &
