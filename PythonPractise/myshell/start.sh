#!/bin/bash
# Start upgrade MATS application
if
	source ./scripts/common.sh
then
	logLevel "[EXECUTION]START"
else
	logLevel "[INTERRUPT]Can't start script, please check you execution path."
	exit 1
fi
#rmLogIfNeed
echo $1
. scripts/check_missing.sh $1 $2
. scripts/app_upgrade.sh $1 $2
. scripts/copysql_exscutemigratesql.sh $1 $2
logLevel "[EXECUTION]END"
