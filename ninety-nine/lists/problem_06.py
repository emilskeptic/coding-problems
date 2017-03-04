#!/usr/bin/env python

# Name:             problem_06.py
# Purpose:          List palindrome checker.
# Author:           github.com/emilskeptic
# Last modified:    2017-03-04
# Version:          1.0
# Depends on:       Python 3.5+

def list_palindrome_checker(my_list):
    if my_list == my_list[::-1]:
        return True
    else:
        return False

foo = [1, 2, 3, 4, 5, 6]
bar = [1, 2, 3, 3, 2, 1]

print(list_palindrome_checker(foo))
print(list_palindrome_checker(bar))
