import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a_line = list(map(int, input().split()))
    b_line = list(map(int, input().split()))

    dp = [[0] * n for _ in range(2)]
    dp[0][0], dp[1][0] = a_line[0], b_line[0]
    dp[0][1], dp[1][1] = a_line[1] + dp[1][0], b_line[1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1], dp[0][i - 2], dp[1][i - 2]) + a_line[i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2], dp[1][i - 2]) + b_line[i]
    #print(dp[0], dp[1], sep='\n')
    print(max(dp[1][-1], dp[0][-1]))
