#!/usr/bin/env python

# Name:             problem_14.py
# Purpose:          Sequential duplication of list items.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

def duplicate_sequentially(my_list):
    final = []
    for item in my_list:
        final.append(item)
        final.append(item)
    return final

foo = ["a", "b", "c", "d"]
print(duplicate_sequentially(foo))
