#!/usr/bin/env python

# Name:             problem_28.py
# Purpose:          Sorts sublists by size.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

def sort_sublists(my_list):
     return sorted(my_list, key=len)

foo = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"], ["d", "e"],
       ["i", "j", "k", "l"], ["m", "n"], ["o"]]

print(sort_sublists(foo))
