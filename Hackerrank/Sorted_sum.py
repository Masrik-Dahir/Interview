#!/bin/python3


import os


class Operation:
    def __init__(self, size):
        self.lenght = size
        self.array = [0 for _ in range(self.lenght)]

    def addition(self, curr, value):
        if curr == 0:
            self.array[0] += value
            return
        while curr < self.lenght:
            self.array[curr] += value
            curr += curr & (-curr)

    def find(self, curr):
        if curr < 0:
            return 0
        answer = self.array[0]
        while curr > 0:
            answer += self.array[curr]
            curr &= curr - 1
        return answer


def sortedSum(a):
    max = 10 ** 6
    constraint = 10 ** 9 + 7
    before = Operation(max + 1)
    after = Operation(max + 1)
    current = result = sum_all = 0
    for i in range(len(a)):
        curr_position = before.find(a[i]) + 1
        biggest = sum_all - after.find(a[i])
        current = (current + curr_position * a[i] + biggest) % constraint
        result = (result + current) % constraint
        before.addition(a[i], 1)
        after.addition(a[i], a[i])
        sum_all += a[i]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = sortedSum(a)

    fptr.write(str(result) + '\n')

    fptr.close()