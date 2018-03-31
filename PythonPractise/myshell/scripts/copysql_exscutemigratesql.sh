#!/bin/bash
# Copy sql to migrate folder
source ./scripts/common.sh
currentPath=`pwd`
migratefolder="$TAS_HOME/migrate"
migrateSqlscriptArray=()
newmigrateSqlscriptArray=()
check_migrateFolder(){
if [ ! -d $migratefolder ];then
   logLevel "[INFO]migrate doesn't exist in tashome,create migrate folder  "
   mkdir $migratefolder
fi
}
copySqlScriptToMigrate(){
if [ $# != 4 ];then
		echo "[INTERRUPT]Wrong arg,please input three args"
		exit 1
fi
    local array=($3)
    local benchmark="migratesql"
    echo ${array[@]}
	local sqlfolder=$2
	local buildnumber=$1
	i=0
	for sql in ${array[@]}
	do 
	    if [ "$sqlfolder" == "$benchmark" ];then
		    ifExist $migratefolder/$sql
		    if [ $? = 1 ];then
			    logLevel "[INFO]$sql existing, continue..."
		    else
			    logLevel "[INFO]copy $sql to $migratefolder"
			    cp $currentPath/$4/$buildnumber/$sqlfolder/$sql $migratefolder
                            sleep 2s
                            logLevel "[INFO]Record new migratesql $sql to query"
                            newmigrateSqlscriptArray[$i]=$sql
                            i=`expr $i + 1`
                            		
		    fi
			   
	    else
		    logLevel "[INFO]copy $sql to $migratefolder "
	            cp $currentPath/$4/$buildnumber/$sqlfolder/$sql $migratefolder
	    fi
         done

}

get_migratesql(){
    local buildnumber=$1
	i=0
	for file in $( ls "$currentPath/$2/$buildnumber/migratesql" )
	do
	  logLevel "[INFO]$file exists"
	  migrateSqlscriptArray[$i]=$file
	  i=`expr $i + 1`
          echo $i
        done

}
executeMigrateScripts(){
if [ $# != 1 ];then
	echo "[INTERRUPT]Wrong arg,please input one arg"
	exit 1
fi
local array=($1)
#tee ./temp.log
for sql in  ${array[@]}
do

  logLevel  "[INFO]execute migratesql screipt $sql "
  $TAS_HOME/prod/unix/script/sqltasdb.sh $migratefolder/$sql
       
done

#cat ./temp.log >> $LOG_FILE
}

logLevel "[INFO]getMigrateSqlArray"
get_migratesql "$1" "$2"
echo ${migrateSqlscriptArray[@]}
logLevel "[INFO]check migrate folder whether exists in tashome  "
check_migrateFolder
logLevel "[INFO]start copy table sql scripts "
copySqlScriptToMigrate "$1" "sql" "${sqlscriptArray[*]}" "$2"
logLevel "[INFO]start copy migrate sql scripts "
copySqlScriptToMigrate "$1" "migratesql" "${migrateSqlscriptArray[*]}" "$2"
logLevel "[INFO]start execute migrate sql scripts"
executeMigrateScripts "${newmigrateSqlscriptArray[*]}"
startServiceIfNeeded


