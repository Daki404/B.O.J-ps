import sys, heapq
input = sys.stdin.readline


def dijkstra(st, road):
    cost = {node: float('inf') for node in road}
    cost[st] = 0
    queue = [[cost[st], st]]

    while queue:
        dis, node = heapq.heappop(queue)
        if dis > cost[node]: continue
        for i, j in road[node].items():
            node_dis = dis + j
            if node_dis > cost[i]: continue
            cost[i] = node_dis
            heapq.heappush(queue, [cost[i], i])
    return cost


n, m = map(int, input().split())

road = {i: {} for i in range(1, n + 1)}

for _ in range(m):
    st, ed, cost = map(int, input().split())
    road[st][ed] = cost
    road[ed][st] = cost

v_fix1, v_fix2 = map(int, input().split())

st = dijkstra(1, road)
point_1 = dijkstra(v_fix1, road)
point_2 = dijkstra(v_fix2, road)

a = st[v_fix1] + point_1[v_fix2] + point_2[n]
b = st[v_fix2] + point_2[v_fix1] + point_1[n]

ans = min(a, b)
if ans == float('inf'): print(-1)
else: print(ans)