import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())

road = {i: {} for i in range(1, n + 1)}
for _ in range(m):
    st, ed, cost = map(int, input().split())
    road[st][ed] = cost


def dijkstra(st, road):
    cost = {node: float('inf') for node in road}
    cost[st] = 0
    queue = [[cost[st], st]]

    while queue:
        distance, node = heapq.heappop(queue)
        if distance > cost[node]: continue

        for i, j in road[node].items():
            v_distance = distance + j
            if v_distance < cost[i]:
                cost[i] = v_distance
                heapq.heappush(queue, [v_distance, i])
    return cost


go_road = {i: dijkstra(i, road)[x] for i in range(1, n + 1) if i != x}
back_road = dijkstra(x, road)

for i, j in go_road.items():
    back_road[i] += j

print(max(back_road.values()))