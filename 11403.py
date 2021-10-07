from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(st):
    stack = [[[], st]]
    visit = [False] * len(field)

    while stack:
        way, aim = stack.pop()
        for i in way:
            field[i][aim] = 1
        way += [aim]
        for i in graph[aim]:
            if not visit[i]:
                stack.append([way, i])
                visit[i] = True


graph = defaultdict(list)
field = []
n = int(input())

for _ in range(n):
    field.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if field[i][j]:
            graph[i].append(j)

for i in range(n):
    dfs(i)

for i in field:
    print(*i)