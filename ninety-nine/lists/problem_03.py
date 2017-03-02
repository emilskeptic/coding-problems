#!/usr/bin/env python

# Name:             problem_03.py
# Purpose:          Finds element k in a list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-02
# Version:          1.0
# Depends on:       Python 3.5+

def kth_element_of_list(k, my_list):
    return my_list[k-1]

star = [23, -4, "cake", 55, 22, 12, -21, "foo"]
element = 5
print(kth_element_of_list(5, star))
