#!/usr/bin/env python

# Name:             problem_22.py
# Purpose:          Create a list containing integers in a specific range.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

def integer_range(start,end):
    return list(range(start,end+1))

print(integer_range(4,9))
