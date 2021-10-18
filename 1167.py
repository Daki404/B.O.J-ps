import sys
input = sys.stdin.readline


def dfs_st():
    visit = [False] * (n + 1)
    stack = [1]

    while stack:
        v = stack.pop()
        for i, j in graph[v]:
            if visit[i]: continue
            visit[i] = True
            stack.append(i)
    return v


def dfs_tree(visit):
    max_num = 0
    visit_ = visit.copy()

    def sol(n):
        nonlocal max_num, visit_
        visit_[n], stack = True, [(n, 0)]
        while stack:
            v, num = stack.pop()
            max_num = max(max_num, num)
            for i, j in graph[v]:
                if visit_[i]: continue
                visit_[i] = True
                stack.append((i, num + j))
        for i, j in visit_.items():
            if not j: return 'not_end', i
        else: return 'end', max_num
    return sol


n = int(input())
graph = {i: list() for i in range(1, n + 1)}
visit = {}
for i in range(1, n + 1):
    line = list(map(int, input().split()))[:-1]
    visit[line[0]] = False
    for j in range(1, len(line), 2):
        graph[line[0]].append((line[j], line[j + 1]))

ans = 0

a = dfs_st()
while True:
    com, tmp = dfs_tree(visit)(a)
    if com == 'end':
        ans = max(ans, tmp)
        break
    else:
        a = tmp

print(ans)


