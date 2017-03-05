#!/usr/bin/env python

# Name:             problem_01.py
# Purpose:          Find out if an integer is a prime or not.
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
        return True
    else:
        return False

print(prime_finder(7))
print(prime_finder(28))
