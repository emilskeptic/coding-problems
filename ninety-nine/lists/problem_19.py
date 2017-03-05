#!/usr/bin/env python

# Name:             problem_19.py
# Purpose:          Rotate a list k places to the left.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

def rotate_list(my_list, rotation):
    L1 = my_list[0:rotation]
    L2 = my_list[rotation:len(my_list)]
    return L2 + L1

foo = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(rotate_list(foo, 3))
print(rotate_list(foo, -2))
