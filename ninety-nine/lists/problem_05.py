#!/usr/bin/env python

# Name:             problem_04.py
# Purpose:          Reverses a list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

def reverse_list(my_list):
    return my_list[::-1]

foo = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(foo))
