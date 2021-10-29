# boj - 11404, 플로이드, https://www.acmicpc.net/problem/11404
import sys
input = sys.stdin.readline

city_len = int(input())
bus_len = int(input())
bus_dp = [[float('inf')] * city_len for _ in range(city_len)]

for _ in range(bus_len):
    st, ed, cost = map(int, input().split())
    bus_dp[st - 1][ed - 1] = min(bus_dp[st - 1][ed - 1], cost)

for k in range(city_len):
    bus_dp[k][k] = 0
    for i in range(city_len):
        for j in range(city_len):
            bus_dp[i][j] = min(bus_dp[i][j], bus_dp[i][k] + bus_dp[k][j])

for i in bus_dp:
    for j in i:
        if j == float('inf'):
            print(0, end=' ')
        else: print(j, end=' ')
    print()
