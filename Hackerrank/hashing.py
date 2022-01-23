#!/bin/python3

import math
import os
import random
import re
import string
import sys


#
# Complete the 'sortedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


asci = 131
add_operation = [""] + list(string.ascii_letters) + [str(d) for d in range(10)]
operation = [asci ** i for i in range(11)]
modulas = 10 ** 9 + 7

def hashing(given):
    current = 0
    for i in range(len(given)):
        current += ord(given[-(i + 1)]) * operation[i]
    return current % modulas

def authEvents(events):
    # Write your code here
    hash = None
    result = []
    for event, outcome in events:
        if event == "setPassword":
            hash = set(hashing(outcome + occurrence) for occurrence in add_operation)
        else:
            assert event == "authorize"
            result.append(1 if int(outcome) in hash else 0)
    return result