import sys
input = sys.stdin.readline

n, m = map(int, input().split())
line = [0] + list(map(int, input().split()))

for i in range(1, len(line)):
    line[i] += line[i - 1]


for _ in range(m):
    a, b = map(int, input().split())
    print(line[b] - line[a-1])
