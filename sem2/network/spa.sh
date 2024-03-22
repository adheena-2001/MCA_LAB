#!/bin/bash
echo "Please enter first number"
read a
echo "Please enter second number"
read b
echo "Please enter third number"
read c
echo "Please enter fourth number"
read d
s=$(($a + $b + $c + $d))
p=$(($a * $b * $c * $d))
a=$(($s/4))
echo "Sum=" $s
echo "Product=" $p
echo "Average=" $a


