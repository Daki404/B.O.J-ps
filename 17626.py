import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    val = sys.maxsize
    j = 1
    while (j ** 2) <= i:
        val = min(val, dp[i - (j ** 2)])
        j += 1
    dp.append(val + 1)

print(dp[-1])