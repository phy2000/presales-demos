#!/bin/bash 

ROLEARN=arn:aws:iam::368099029718:role/training-10.2-2017q4-firehose_delivery_role
BUCKETARN=arn:aws:s3:::presales-training-102-2017q4


SCRIPTDIR=$(cd $(dirname $0) && pwd)
NAMELIST=$SCRIPTDIR/usernames.txt

if [ ! -z $1 ] ; then
NAMELIST=$1
fi

if [ ! -r $NAMELIST ] ; then
    echo file "$NAMELIST not found!" >&2
    exit -1
fi

START=18
END=20

cd $SCRIPTDIR
for NUM in $(seq -w $START $END) ; do
    name=user$NUM

    S3CONFIG="--s3-destination-configuration \
RoleARN=$ROLEARN,BucketARN=$BUCKETARN,Prefix=firehose/$name/,\
CompressionFormat=UNCOMPRESSED,EncryptionConfiguration={NoEncryptionConfig=NoEncryption},\
CloudWatchLoggingOptions={Enabled=false}"

    echo S3CONFIG=$S3CONFIG
    echo -n $name... 
    while ! aws firehose create-delivery-stream --delivery-stream-type DirectPut --delivery-stream-name training-firehose-$name $S3CONFIG
    do
        echo WAITING...
        sleep 20
    done
    echo $name OK
    sleep 1
done

