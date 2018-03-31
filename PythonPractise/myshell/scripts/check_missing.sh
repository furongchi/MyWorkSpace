#!/bin/bash
# Check if script is used correctly, and no missing for files
# TBD change log description
source ./scripts/common.sh

currentPath=`pwd`

checkScriptsArray() {
	logLevel "[INFO]checkScriptsArray"
	checkItCorrect "$currentPath/scripts" "${scriptsArray[*]}"
}
checkSqlScriptArray() {
    
	logLevel "[INFO]checkSqlScriptArray"
	checkItCorrect "$currentPath/$2/$1/sql" "${sqlscriptArray[*]}" 
}
checkAppsArray() {
	logLevel "[INFO]checkAppsArray"
	checkItCorrect "$currentPath/$2/$1/app"  "${appsArray[*]}"
}
logLevel "[FUNCTION]checkScriptsArray"
checkScriptsArray
logLevel "[FUNCTION]checkSqlScriptArray"
checkSqlScriptArray $1 $2
logLevel "[FUNCTION]checkAppsArray"
checkAppsArray $1 $2
