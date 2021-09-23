import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    book = list(map(int, input().split()))

    dp = [0] * (n + 1)
    for i in range(1, )