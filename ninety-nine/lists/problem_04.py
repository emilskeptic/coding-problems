#!/usr/bin/env python

# Name:             problem_04.py
# Purpose:          Finds the number of elements in a list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

def list_length(my_list):
    return len(my_list)

foo = [1, 5, 21, -4, -3, "hello", "nope", "snake"]
print(list_length(foo))
