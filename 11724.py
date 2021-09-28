from collections import defaultdict
import sys

input = sys.stdin.readline


def dfs_counter(graph, n):
    visit = [True] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if visit[i]:
            cnt += 1
            stack = [i]
            while stack:
                new_v = stack.pop()
                visit[new_v] = False
                for j in graph[new_v]:
                    if visit[j]:
                        stack.append(j)

    return cnt


n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)

print(dfs_counter(graph, n))