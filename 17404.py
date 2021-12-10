import sys
input = sys.stdin.readline


def sol(n):

    def dp_sol(st):
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][st] = house[0][st]

        for i in range(1, n):
            dp[i][0] = house[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = house[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = house[i][2] + min(dp[i - 1][1], dp[i - 1][0])

        return min(dp[n - 1][i] for i in range(3) if i != st)

    return min(dp_sol(0), dp_sol(1), dp_sol(2))


n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
print(sol(n))



