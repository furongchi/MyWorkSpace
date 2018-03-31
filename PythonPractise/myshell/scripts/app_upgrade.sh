#!/bin/bash
#Used for dependencies and application installation
source ./scripts/common.sh
currentPath=`pwd`
deployPath="$TAS_HOME/var/jsvr/tasmib/deployments"
install_app(){
    stop_tas
	if [ $? = 1 ];then
			
			if
			    cp -r $currentPath/$2/$1/app/* $deployPath
			then
		        logLevel "[INFO]Install MATS application is successful, continue..."
	        else
		        logLevel "[INTERRUPT]Install MATS application is fail, exit"
		        exit 1
		    fi
			
	else
		logLevel "tas stops failed,please check "
		exit 1
	fi
}
logLevel "copy app package to deployments"
install_app $1 $2
