import sys
input = sys.stdin.readline


for _ in range(int(input())):
    line = list(map(int, input().split()))
    minute_sum = 0
    for i, j in enumerate(line):
        minute_sum += (i + 1) * j
    print(minute_sum % 2)