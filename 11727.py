import sys
input = sys.stdin.readline

dp = [0] * 1000
dp[0], dp[1] = 1, 3

n = int(input())
for i in range(2, n):
    dp[i] += dp[i - 1]
    dp[i] += dp[i - 2] * 2

print(dp[n-1] % 10007)

