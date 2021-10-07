import sys
input = sys.stdin.readline


def dfs(v):
    for i in range(n):
        if visit[i] == 0 and field[v][i] == 1:
            visit[i] = 1
            dfs(i)


n = int(input())
field = []
for _ in range(n):
    field.append(list(map(int, input().split())))

for i in range(n):
    visit = [0] * n
    dfs(i)
    for j in range(n):
        if visit[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()