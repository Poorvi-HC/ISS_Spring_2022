#!/bin/bash
if [[ $# == 2 ]];
then
	let a=$1 b=$2
	expr $a \* $b

else
	echo "Error"
fi



