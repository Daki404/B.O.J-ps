import sys, heapq
input = sys.stdin.readline


def solve(n, graph):
    ans = 0

    def dfs(n):
        visit = [False] * (island + 1)
        visit[n] = True
        tmp = farming[n]
        stack = [(n, 0)]

        while stack:
            v, cost = stack.pop()
            if not visit[v]:
                tmp += farming[v]
                visit[v] = True
            for i, j in graph[v].items():
                if cost + j > search: continue
                stack.append((i, cost + j))
        return tmp
    for i in range(1, island + 1):
        ans = max(ans, dfs(i))
    return ans


island, search, road = map(int, input().split())
farming = {}

for i, j in enumerate(list(map(int, input().split()))):
    farming[i + 1] = j


graph = {i: {} for i in range(1, island + 1)}
for _ in range(road):
    st, ed, cost = map(int, input().split())
    if graph[st].get(ed) is None: graph[st][ed] = cost
    else: graph[st][ed] = min(cost, graph[st][ed])
    if graph[ed].get(st) is None: graph[ed][st] = cost
    else: min(cost, graph[ed][st])

print(solve(island, graph))