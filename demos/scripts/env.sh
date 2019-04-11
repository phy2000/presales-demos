export INFA_HOME=/opt/infa/current
export JAVA_HOME=$INFA_HOME/tools/debugtools/java/

export KAFKA_HOME=/opt/kafka/current/
export PATH=/opt/kafka/scripts:$PATH
export KAFKA_CONFIG=$KAFKA_HOME/config
export KAFKA_BIN=$KAFKA_HOME/bin
export KAFKA_HOST=quickstart.cloudera
export KAFKA_PORT=9092
export PWX_HOME=/opt/infa/PowerExchange10.2.0
export PWX_CONFIG=$PWX_HOME/dbmover.cfg
export PWX_LICENSE=$PWX_HOME/license.key
export PWXPUB_HOME=/opt/infa/pwxcdcpub110
export KAFKA_CLIENT_LIBS=$KAFKA_HOME/libs
export PWX_CMDS=/var/scripts/cdc/pwx
export PWXPUB_CMDS=/var/scripts/cdc/pub
export PATH=$PATH:$PWX_HOME
if [ -z "$ORACLE_HOME" ] ; then
source /u01/app/oracle/product/11.2.0/xe/bin/oracle_env.sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWX_HOME:$ORACLE_HOME/lib
fi
echo $LD_LIBRARY_PATH
export CONFLUENT_HOME=/opt/confluent/current
export CONFLUENT_CURRENT=$CONFLUENT_HOME/working
export CHOME=$CONFLUENT_HOME
