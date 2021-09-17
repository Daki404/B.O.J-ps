import sys
input = sys.stdin.readline


def sol(graph, v):
    node = graph.keys()

    visit = [True] * (v + 1)
    color = [None] * (v + 1)

    def dfs(st):
        stack = [(st, True)]
        while stack:
            new_v, stat = stack.pop()
            if visit[new_v] == True:
                visit[new_v] = False
                if stat: color[new_v] = 1
                else: color[new_v] = 0
                for i in graph[new_v]: stack.append((i, not stat))

    for i in node:
        if visit[i]: dfs(i)

    for i in node:
        for j in graph[i]:
            if color[i] == color[j] and i != j: return 'NO'

    return 'YES'


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = {}
    for _ in range(e):
        a, b = map(int, input().split())
        if graph.get(a):
            graph[a].append(b)
        else:
            graph[a] = [b]
        if graph.get(b):
            graph[b].append(a)
        else:
            graph[b] = [a]
    #print(graph)
    print(sol(graph, v))
