import sys, heapq
input = sys.stdin.readline


def dijkstra(n, road):
    road_cost = {i: float('inf') for i in range(1, city + 1)}
    road_cost[n] = 0
    queue = [(0, n)]

    while queue:
        cost, v = heapq.heappop(queue)
        if cost > road_cost[v]: continue
        for node in road[v]:
            if road_cost[node] > (new_cost := road[v][node] + cost):
                road_cost[node] = new_cost
                heapq.heappush(queue, (new_cost, node))
    return road_cost


city = int(input())
bus = int(input())

bus_cost = {i: {} for i in range(1, city + 1)}
for _ in range(bus):
    st, ed, cost = map(int, input().split())
    if bus_cost[st].get(ed) is not None:
        bus_cost[st][ed] = min(bus_cost[st][ed], cost)
    else: bus_cost[st][ed] = cost

st, ed = map(int, input().split())
print(dijkstra(st, bus_cost)[ed])
