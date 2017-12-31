#!/bin/python

import sys

n = str(bin(int(raw_input()))[2:]).split('0')

n.sort()

print len(n[len(n)-1])