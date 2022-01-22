#!/bin/python3
import math
import os
import random
import re
import sys

# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.
# Input Format
# A single line of input containing the full name, .
# Constraints
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
# Output Format
# Print the capitalized string, .
# Sample Input
# chris alan
# Sample Output
# Chris Alan
# _____________________________________________________________________________________________________________________________________________________________________________________________________________


def solve(s):
    li = s.split(" ")
    for i in range(0, len(li)):
        word = ""
        for j in range(0, len(li[i])):
            if j == 0:
                # print(i[j].upper())
                word += li[i][j].upper()
            else:
                word += li[i][j]
        li[i] = word

    result = ""
    for i in range(0, len(li)):
        if i == 0:
            result += li[i]
        else:
            result += " " + li[i]

    return result


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)