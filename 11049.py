import sys
input = sys.stdin.readline


def sol():
    for i in range(1, n):
        for j in range(n - i):
            x = i + j
            dp[j][x] = 2 ** 32
            for k in range(j, x):
                dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + field[j][0] * field[k][1] * field[x][1])
    return dp[0][n-1]


n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

print(sol())