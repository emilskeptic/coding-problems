#!/usr/bin/env python

# Name:             problem_16.py
# Purpose:          Removes every kth element from a list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

def drop_every_kth_element(my_list, k):
    for item in my_list:
        if (my_list.index(item)) % (k-1) == 0 and (my_list.index(item)) != 0:
            del my_list[my_list.index(item)]
    return my_list

foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(drop_every_kth_element(foo, 3))
