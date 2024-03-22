#!/bin/bash

check_odd_even() {
    number=$1
    if [ $((number % 2)) -eq 0 ]; then
        echo "$number is an even number."
    else
        echo "$number is an odd number."
    fi
}

# Input a number to check whether it's odd or even
read -p "Enter a number: " input_number

# Call the check_odd_even function
check_odd_even $input_number

