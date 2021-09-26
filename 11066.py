import sys
input = sys.stdin.readline
MAX = sys.maxsize

for _ in range(int(input())):
    n = int(input())
    pages = [0] + list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]

    for i in range(1, n + 1):
        pages[i] += pages[i - 1]

    for i in range(1, n):
        for j in range(n - i):
            k = i + j
            dp[j][k] = MAX
            for l in range(j, k):
                dp[j][k] = min(dp[j][k], dp[j][l] + dp[l + 1][k] - pages[j] + pages[k + 1])

    print(dp[0][n-1])
