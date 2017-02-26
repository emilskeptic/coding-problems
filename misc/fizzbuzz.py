#!/usr/bin/env python

# Name:             fizzbuzz.py
# Purpose:          Completes the classic coding problem "FizzBuzz".
# Author:           github.com/emilskeptic
# Last modified:    2017-02-26
# Version:          1.0
# Depends on:       Python 3.5+

for number in range(1,101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
