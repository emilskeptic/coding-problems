#!/usr/bin/env python

# Name:             problem_20.py
# Purpose:          Removes and save every kth element from a list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

leftovers = []

def remove_and_save_every_kth_element(my_list, k):
    for item in my_list:
        if (my_list.index(item)) % (k-1) == 0 and (my_list.index(item)) != 0:
            leftovers.append(item)
            del my_list[my_list.index(item)]
    print("Cleaned list is: ", my_list)
    print("Removed list items are: ", leftovers)

foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_and_save_every_kth_element(foo, 3)
