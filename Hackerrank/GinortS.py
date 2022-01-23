#!/bin/python3

# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# You are given a string .
#  contains alphanumeric characters only.
# Your task is to sort the string  in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Input Format
# A single line of input contains the string .
# Constraints
# Output Format
# Output the sorted string .
# Sample Input
# Sorting1234
# Sample Output
# ginortS1324
# _____________________________________________________________________________________________________________________________________________________________________________________________________________


def lis_to_str(lis):
    a = ""
    for i in lis:
        a += str(i)
    return a


def sort(val):
    word = ""
    li = []
    for i in val:
        li.append(i)
    li.sort()
    lower = []
    upper = []
    even = []
    odd = []

    for i in li:
        if (i == i.lower() and not i.isdigit()):
            lower.append(i)

    for i in li:
        if (i == i.upper() and not i.isdigit()):
            upper.append(i)

    for i in li:
        if (i.isdigit() and int(i) % 2 == 0):
            even.append(i)

    for i in li:
        if (i.isdigit() and int(i) % 2 == 1):
            odd.append(i)

    return lis_to_str(lower) + lis_to_str(upper) + lis_to_str(odd) + lis_to_str(even)


print(sort(input()))