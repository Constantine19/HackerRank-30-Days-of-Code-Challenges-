#!/bin/python

import sys

n = int(raw_input().strip())
arr = raw_input().strip().split(' ')

arr2 = []

for i in reversed(range(n)):
    arr2.append(arr[i])
print ' '.join(arr2)