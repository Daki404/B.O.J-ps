from collections import Counter
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    line = list(map(int, input().split()))
    one = zero = 0
    for i in line:
        if i == 1: one += 1
        elif i == 0: zero += 1
    if zero: print(one * (zero * 2))
    else: print(one)