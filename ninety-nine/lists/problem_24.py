#!/usr/bin/env python

# Name:             problem_24.py
# Purpose:          Simple lotto.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

import random

def lotto(numbers, highest):
    winning_numbers = []
    for i in list(range(1,numbers+1)):
        winning_numbers.append(random.choice(list(range(1,highest+1))))
    return winning_numbers

print(lotto(6,49))
