#!/usr/bin/env python

# Name:             problem_01.py
# Purpose:          Find all prime divisors.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-05
# Version:          1.0
# Depends on:       Python 3.5+

def prime_finder(number):
    divisors = []
    for i in list(range(2,round((number+1)/2))):
        if number % i == 0:
            divisors.append(i)
        else:
            pass
    if len(divisors) == 0:
        divisors.append(1)
        divisors.append(number)
        return divisors
    else:
        return sorted(divisors)

print(prime_finder(7))
print(prime_finder(28))
