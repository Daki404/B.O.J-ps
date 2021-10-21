import sys
input = sys.stdin.readline


def dfs(n, graph) -> (int, int):  # deepest (node, distance) return
    visit = [False] * (len(graph) + 1)
    visit[n] = True
    stack = [[n, 0]]
    ans = (0, 0)  # node, cost for compare

    while stack:
        v, cost = stack.pop()
        for i, j in graph[v].items():
            if not visit[i]:
                visit[i] = True
                tmp_cost = cost + j
                if ans[1] < tmp_cost:  # find max-cost node
                    ans = (i, tmp_cost)
                stack.append([i, tmp_cost])
    return ans


n = int(input())

if n == 1: print(0)  # if not exist edge
else:
    graph = {i: {} for i in range(1, n + 1)}

    for _ in range(n - 1):
        st, ed, cost = map(int, input().split())
        graph[st][ed] = cost
        graph[ed][st] = cost

    deepest_node, deepest_cost = dfs(1, graph)  # deepest node from root
    print(dfs(deepest_node, graph)[1])  # deepest node from prior deepest node