#!/usr/bin/env python

# Name:             problem_23.py
# Purpose:          Extract k number of random elements from a list.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

import random

final = []

def random_list_slice(my_list, k):
    for i in list(range(1,k+1)):
        final.append(random.choice(my_list))
    return final

foo = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(random_list_slice(foo, 3))
