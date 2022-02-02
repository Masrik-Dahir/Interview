# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
#
# Example
#
#
# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
#
# Function Description
#
# Complete the sockMerchant function in the editor below.
#
# sockMerchant has the following parameter(s):
#
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns
#
# int: the number of pairs
# Input Format
#
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the socks in the pile.
#
# Constraints
#
#  where
# Sample Input
#
# STDIN                       Function
# -----                       --------
# 9                           n = 9
# 10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# Sample Output
#
# 3
# Explanation
#
# sock.png
#
# There are three pairs of socks.


def sockMerchant(n, ar):
    # Write your code here
    count = 0
    dic = {}

    for i in range(0, len(ar)):
        if ar[i] not in dic.keys():
            dic[ar[i]] = 1
        else:
            dic[ar[i]] += 1
    for i, j in dic.items():
        if j % 2 == 1:
            count += (j - 1) / 2
        else:
            count += j / 2

    return int(count)
