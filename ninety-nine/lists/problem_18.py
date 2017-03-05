#!/usr/bin/env python

# Name:             problem_18.py
# Purpose:          Slices a list with both boudaries being inclusive.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

def slice_inclusive(my_list, start, end):
    return my_list[start-1:end]

foo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(slice_inclusive(foo, 3, 7))
