#!/bin/python3

# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:
# #size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
# #size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
# #size 10
# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------
# The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).
# Function Description
# Complete the rangoli function in the editor below.
# rangoli has the following parameters:
# int size: the size of the rangoli
# Returns
# string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
# Input Format
# Only one line of input containing , the size of the rangoli.
# Constraints
# Sample Input
# 5
# Sample Output
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
# _____________________________________________________________________________________________________________________________________________________________________________________________________________


def lis_to_str(lis):
    s = ""
    for i in lis:
        s += str(i)
    return s

def print_rangoli(size):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    g_lis = []
    for row in range(0, size * 2 - 1):
        lis = []
        row = abs(row - size + 1)
        for i in range(size - 1, row - 1, -1):
            lis.append(alphabet[i])
            if i > row:
                lis.append("-")
        # print(lis)
        lis_reverse = []
        for i in range(row, size):
            lis_reverse.append(alphabet[i])
            if i < size - 1:
                lis_reverse.append("-")
        # print(lis_reverse)

        for i in range(1, len(lis_reverse)):
            if i != 0:
                lis.append(lis_reverse[i])
        g_lis.append(lis)

    for col in range(0, len(g_lis)):
        hyphen = (size * 2 - 1 + size * 2 - 2 - len(g_lis[col])) / 2
        for i in range(0,int(hyphen)):
            g_lis[col].append("-")
        for i in range(0,int(hyphen)):
            g_lis[col].insert(0,"-")

    for i in g_lis:
        print(lis_to_str(i))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
