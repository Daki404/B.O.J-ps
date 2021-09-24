import sys, math
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    book = list(map(int, input().split()))
    dp = [[math.inf] * n for _ in range(n)]
    for i, j in enumerate(book):
        dp[i][i] = j
    for i in range(n):
        for j in range(n - i):
            for k in range(j, i + j):
                if i <= 1:
                    dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j])
                else:
                    dp[j][i + j] = min(dp[j][i + j], (dp[j][k] + dp[k + 1][i + j]) * 2)
    print(dp[0][n-1])