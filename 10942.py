import sys
input = sys.stdin.readline


n = int(input())
line = list(map(int, input().split()))
dp = [[1] * n for _ in range(n)]

for idx, val in enumerate(line):
    dp[idx][idx] = 1

for i in range(1, n):
    for j in range(n - i):
        k = i + j
        if dp[j + 1][k - 1] and line[j] == line[k]:
            dp[j][k] = 1
        else:
            dp[j][k] = 0

for _ in range(int(input())):
    st, ed = map(int, input().split())
    print(dp[st - 1][ed - 1])
