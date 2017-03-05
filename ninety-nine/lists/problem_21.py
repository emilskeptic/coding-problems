#!/usr/bin/env python

# Name:             problem_21.py
# Purpose:          Insert element at a certain position in a list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

def insert_element_at_position(my_list, position, element):
    return my_list[:position-1] + [element] + my_list[position-1:]

foo = ["a", "b", "c", "d"]
print(insert_element_at_position(foo, 2, "alfa"))
