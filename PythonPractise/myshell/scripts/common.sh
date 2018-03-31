#!/bin/bash
# Program:
# 	Common functions used in installation

startTime=`date +%Y%m%d%H%M%S`
LOG_FILE="execution_$startTime.log"

breakMark="/"

## DO NOT change the definations, unless you know what you are doing
scriptsArray=("check_missing.sh" "common.sh" "app_upgrade.sh" "copysql_exscutemigratesql.sh")

sqlscriptArray=("mat-createtbls-mysql.sql" "mat-createcust-mysql.sql")
migrateSqlscriptArray=()
appsArray=("mataweb.ear" "mat.ear" "matiweb.ear"  "matsweb.ear" )

rmLogIfNeed() {
	if [ -f $LOG_FILE ];then
		rm -rf $LOG_FILE
	fi
}

log() {
	local currentTime=`date +"%Y-%m-%d %H:%M:%S"`
	echo $currentTime" | "$1 2>&1 | tee -a $LOG_FILE
}

logLevel() {
	local currentTime=`date +"%Y-%m-%d %H:%M:%S"`
	echo $currentTime" | [LEVEL1] "$1 2>&1 | tee -a $LOG_FILE
}

checkItCorrect() {
	local scriptDir=$1
	local array=($2)
	logLevel "[CHECK]Start to check:"$scriptDir",  array:""${array[*]}"
	for f in ${array[@]}
	do
		ifExist $scriptDir$breakMark$f
		if [ $? = 1 ];then
			logLevel "[INFO]${f} existing, continue..."
		else
			logLevel "[INTERRUPT]Can't find "${f}", exit"
			exit 1
		fi
	done
	
}

# $1 File type, 1: dir, 2: param, 3: file;
# $2 File name, including a whole path
ifExist() {
	if [ $# -ne 1 ];then
	       echo "[ERROR]Wrong arg,please input one arg"
               exit 1
        fi
	fileCheck=$1
        #log "Try to check "$1", with opr "$opr
	if [ -f $fileCheck ];then
		return 1
	else
		logLevel "[ERROR]$fileCheck is not exist"
		return 0
	fi
}
startServiceIfNeeded() {
        read -p "Do you want to start MATS service now?[Y]" startServiceNow

        if [ $startServiceNow="Y" ];then
            logLevel "[SET]Start service?"$startServiceNow
                tasstart.sh -ml
        elif [ $startServiceNow="y" ];then
            logLevel "[SET]Start service?"$startServiceNow
                tasstart.sh -ml
        else
            logLevel "[SET]Start service?"$startServiceNow
                logLevel "[INFO]Installation is done."
                exit 0
        fi
}
stop_tas(){
    logLevel "stop tas"
        if
            tasstop.sh
        then
                logLevel "[INFO]stop tas successfully, continue..."
                return 1
        else
                logLevel "[INTERRUPT]stop failed, exit"
                exit 1
        fi
}

