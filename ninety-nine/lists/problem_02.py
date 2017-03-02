#!/usr/bin/env python

# Name:             problem_02.py
# Purpose:          Finds second-to-last element of a list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-02
# Version:          1.0
# Depends on:       Python 3.5+

def second_last_element_of_list(my_list):
    return my_list[-2]

bar = [23, -4, "cake", 55]
print(second_last_element_of_list(bar))
