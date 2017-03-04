#!/usr/bin/env python

# Name:             problem_17.py
# Purpose:          Split list into two.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

def split_list(my_list, length):
    L1 = my_list[0:length]
    L2 = my_list[length:len(my_list)]
    return L1, L2

foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(split_list(foo, 4))
