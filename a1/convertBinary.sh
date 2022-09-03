#!/usr/bin/bash

if [ $# -ne 1 ] 
then
echo "This script accepts a single argument in the form of a binary number and returns the integer value"
echo "Usage: ./convertBinary.sh 101010"
exit 1
fi

echo "$((2#${1}))"