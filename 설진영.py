from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def solve(n):
    if bulid.get(n) is None: return cost[n]
    if dp[n]: return dp[n]
    if visit_dp[n] == -1: visit_dp[n] = max(solve(m) for m in bulid[n])
    dp[n] = visit_dp[n] + cost[n]
    return dp[n]


for _ in range(int(input())):
    buliding_num, bulid_num = map(int, input().split())
    cost = {i + 1: j for i, j in enumerate(list(map(int, input().split())))}

    bulid = defaultdict(list)
    for _ in range(bulid_num):
        st, ed = map(int, input().split())
        bulid[ed].append(st)

    destination = int(input())
    dp = [0] * (buliding_num + 1)
    visit_dp = [-1] * ((buliding_num + 1))
    print(solve(destination))