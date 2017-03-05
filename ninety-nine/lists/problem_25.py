#!/usr/bin/env python

# Name:             problem_25.py
# Purpose:          Make random permutation of list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

import random

def random_permutation(my_list):
    random.shuffle(my_list)
    return my_list

foo = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(random_permutation(foo))
