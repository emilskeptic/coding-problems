#!/usr/bin/env python

# Name:             problem_07.py
# Purpose:          Flattens lists.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

flat_list = []

def flatten_list(my_list):
    for item in my_list:
        if isinstance(item, list):
            flatten_list(item)
        else:
            flat_list.append(item)
    return flat_list

foo = ["a", ["b", ["c", "d"], "e"]]

print(flatten_list(foo))
