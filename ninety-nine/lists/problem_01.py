#!/usr/bin/env python

# Name:             problem_01.py
# Purpose:          Finds last element of a list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-02
# Version:          1.0
# Depends on:       Python 3.5+

def last_element_of_list(my_list):
    return my_list[-1]

foo = [1, 4, "error", 34]
print(last_element_of_list(foo))
