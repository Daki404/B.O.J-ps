import sys

input = sys.stdin.readline

m, n = map(int, input().split())
pw = {}

for _ in range(m):
    a, b = input().split()
    pw[a] = b

for _ in range(n):
    a = input().strip()
    print(pw[a])
