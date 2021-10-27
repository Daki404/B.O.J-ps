from collections import deque
import sys
input = sys.stdin.readline


def bfs_tree(st, graph):
    visit = [0] * (n + 1)
    visit[st] = 1
    queue = deque([st])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visit[i]:
                visit[i] = v
                queue.append(i)
    return visit[2:]


n = int(input())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(n - 1):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)

for i in bfs_tree(1, graph):
    print(i)