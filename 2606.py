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


def dfs(st, graph, visit=[]):
    visit.append(st)
    for i in graph[st]:
        if i not in visit:
            visit = dfs(i, graph, visit)
    return visit


print(len(dfs(1, graph)) - 1)
