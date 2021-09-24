import sys
input = sys.stdin.readline


def sol(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    return sol(n-1) + sol(n-2) + sol(n-3)


for _ in range(int(input())):
    print(sol(int(input())))