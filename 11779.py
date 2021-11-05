import sys, heapq
input = sys.stdin.readline


def dijkstra(n, graph):  # dijkstra(heapq) + 경로기록
    road = {i:[float('inf'), [i]] for i in graph}
    road[n][0] = 0
    queue = [(0, n, [n])]

    while queue:
        cost, n, log = heapq.heappop(queue)
        if cost > road[n][0]: continue
        for i, j in graph[n].items():
            if (tmp := cost + j) < road[i][0]:
                road[i][0] = tmp
                road[i][1] = log + [i]
                queue.append((road[i][0], i, road[i][1]))
    return road


city = int(input())
bus = int(input())

graph = {i: {} for i in range(1, city + 1)}
for _ in range(bus):
    st, ed, cost = map(int, input().split())
    if graph[st].get(ed) is None: graph[st][ed] = cost
    else: graph[st][ed] = min(graph[st][ed], cost)

st, ed = map(int, input().split())

result = dijkstra(st, graph)[ed]
print(result[0])
print(len(result[1]))
print(*result[1])
