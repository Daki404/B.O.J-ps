import heapq, sys
input = sys.stdin.readline

v, e = map(int, input().split())

graph = {i: {} for i in range(1, v + 1)}
for _ in range(e):
    st, ed, expense = map(int, input().split())
    if graph[st].get(ed) is None: graph[st][ed] = expense
    else: graph[st][ed] = min(graph[st][ed], expense)
    if graph[ed].get(st) is None: graph[ed][st] = expense
    else: graph[ed][st] = min(graph[ed][st], expense)


def solve(n):
    visit = [False] * (n + 1)
    queue = [(0, 1)]
    ans = 0

    while queue:
        cost, v = heapq.heappop(queue)
        if visit[v]: continue
        visit[v] = True
        ans += cost

        for i, j in graph[v].items():
            heapq.heappush(queue, (j, i))
    return ans


print(solve(v))