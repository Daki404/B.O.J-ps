from collections import deque
import sys
input = sys.stdin.readline

com = int(input())
graph = {}

for _ in range(int(input())):
    st, ed = map(int, input().split())
    if graph.get(st):
        graph[st].append(ed)
    else:
        graph[st] = [ed]
    if graph.get(ed):
        graph[ed].append(st)
    else:
        graph[ed] = [st]


def bfs(st, graph):
    queue = deque([st])
    visit = [st]
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visit:
                visit.append(i)
                queue.append(i)
    return visit


print(len(bfs(1, graph)) - 1)
