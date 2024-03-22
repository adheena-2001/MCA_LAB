#!/bin/bash
echo "Enter the string"
read s
echo $s>temp
reverse="$(rev temp)"
echo "Reversed string:" $reverse
if [ $s = $reverse ]
then
echo "it is palindrome"
else
echo " it is not a Palindrome"
fi
