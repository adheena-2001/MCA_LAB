#!/bin/bash
echo "Enter the year"
read n
num=$(( $n % 4 ))
if [ $num -eq 0 ]
then 
echo "It is a leap year"
else
echo "It is not a leap year"
fi
