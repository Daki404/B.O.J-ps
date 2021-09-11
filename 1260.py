from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = {}

for _ in range(M):
    st, ed = map(int, input().split())
    graph.setdefault(st, [])
    graph[st].append(ed)
    graph.setdefault(ed, [])
    graph[ed].append(st)

for i in graph:
    graph[i].sort()


def dfs(st_v):
    if not graph.get(st_v): return [st_v]
    visit = []
    stack = [st_v]
    while stack:
        v = stack.pop()
        if v not in visit:
            visit.append(v)
            for w in graph[v][::-1]:
                stack.append(w)
    return visit


def bfs(st_v):
    if not graph.get(st_v): return [st_v]
    visit = []
    queue = deque([st_v])
    while queue:
        v = queue.popleft()
        if v not in visit:
            visit.append(v)
            for w in graph[v]:
                queue.append(w)
    return visit


print(*dfs(V))
print(*bfs(V))