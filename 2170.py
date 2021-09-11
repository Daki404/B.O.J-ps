import sys
input = sys.stdin.readline

ans = tmp = 0
line = []

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    line.append((a, b))
line.sort()

left, right = line[0][0], line[0][1]

for i in range(1, n):
    if line[i][0] > right:
        ans += right - left
        left = line[i][0]
        right = line[i][1]
        tmp = 0
    else:
        tmp = line[i][1] - left
        right = max(right, line[i][1])


print(ans + (right - left))