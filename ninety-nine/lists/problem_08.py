#!/usr/bin/env python

# Name:             problem_08.py
# Purpose:          Remove consecutive duplicates.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

clean = []

def remove_consecutive_duplications(my_list):
    before = []
    for item in my_list:
        if item != before:
            clean.append(item)
            before = item
    return clean

foo = ["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"]
print(remove_consecutive_duplications(foo))
