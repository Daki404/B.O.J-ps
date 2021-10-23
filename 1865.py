import sys

input = sys.stdin.readline


def Bellman_ford(st, road):
    dp = [2000000000] * (n + 1)
    dp[st] = 0
    for i in range(n - 1):
        for way in road:
            for node, cost in road[way].items():
                if dp[node] > dp[way] + cost:
                    dp[node] = dp[way] + cost

    for way in road:
        for node, cost in road[way].items():
            if dp[node] > dp[way] + cost:
                return 'YES'
    return 'NO'


for _ in range(int(input())):
    n, m, w = map(int, input().split())
    road = {i: {} for i in range(1, n + 1)}

    for _ in range(m):
        st, ed, cost = map(int, input().split())
        if road[st].get(ed):
            road[st][ed] = min(road[st][ed], cost)
        else: road[st][ed] = cost
        if road[ed].get(st):
            road[ed][st] = min(road[ed][st], cost)
        else: road[ed][st] = cost

    for _ in range(w):
        st, ed, cost = map(int, input().split())
        if road[st].get(ed):
            road[st][ed] = min(road[st][ed], -cost)
        else:
            road[st][ed] = -cost

    print(Bellman_ford(1, road))


