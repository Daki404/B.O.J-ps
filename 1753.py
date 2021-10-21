import sys, heapq

input = sys.stdin.readline


def dijkstra(n, road):
    way = {node: float('inf') for node in road}
    way[n] = 0
    prior_queue = [[0, n]]

    while prior_queue:
        cost, node = heapq.heappop(prior_queue)
        if cost > way[node]: continue
        for i, j in graph[node].items():
            if (new_cost := cost + j) < way[i]:
                way[i] = new_cost
                heapq.heappush(prior_queue, [new_cost, i])
    return way


v, e = map(int, input().split())
go = int(input())

graph = {i: {} for i in range(1, v + 1)}
for _ in range(e):
    st, ed, cost = map(int, input().split())
    if graph[st].get(ed):
        graph[st][ed] = min(graph[st][ed], cost)
    else: graph[st][ed] = cost

ans = []
for i, j in dijkstra(go, graph).items():
    ans.append([i, j])

for i in sorted(ans):
    if i[1] == float('inf'): print('INF')
    else: print(i[1])
