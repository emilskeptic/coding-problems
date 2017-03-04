#!/usr/bin/env python

# Name:             problem_15.py
# Purpose:          Return list where each item occurs Kx number of times.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

final = []

def duplicate_k_times(my_list,times):
    for item in my_list:
        for i in range(1,times+1):
            final.append(item)
    return final

foo = ["a", "b", "c", "d"]
print(duplicate_k_times(foo, 4))
