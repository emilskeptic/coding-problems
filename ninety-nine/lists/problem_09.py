#!/usr/bin/env python

# Name:             problem_09.py
# Purpose:          Pack consecutive duplicates into lists.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

final = []

def pack_consecutive_duplicates(my_list):
    for counter, item in enumerate(my_list):
        if counter == 0 or item != my_list[counter-1]:
            final.append([item])
        else:
            final[-1].append(item)
    for item in final:
        if len(item) == 1:
            final[final.index(item)] = ''.join(item)
    return final

foo = ["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"]
print(pack_consecutive_duplicates(foo))
