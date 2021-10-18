import sys
input = sys.stdin.readline


def dfs(n):
    visit = [False] * (len(graph) + 1)
    visit[n] = True
    stack = [(n, 0)]
    ans = [0, 0]

    while stack:
        v, num = stack.pop()
        if ans[1] < num:
            ans = [v, num]
        for i, j in graph[v]:
            if visit[i]: continue
            visit[i] = True
            stack.append((i, j + num))
    return ans


n = int(input())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(n):
    line = list(map(int, input().split()))
    for i in range(1, len(line) - 2, 2):
        graph[line[0]].append((line[i], line[i + 1]))

ans = 0
st = dfs(1)[0]
print(dfs(st)[1])

