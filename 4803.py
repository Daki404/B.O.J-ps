import sys
input = sys.stdin.readline


def dfs_tree_checker(n):
    stack = [n]
    is_tree = True

    while stack:
        v = stack.pop()
        if visit[v]: is_tree = False
        visit[v] = True
        for i in graph[v]:
            if not visit[i]: stack.append(i)
    return is_tree


idx = 0
while True:
    idx += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0: break

    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        st, ed = map(int, input().split())
        graph[st].append(ed)
        graph[ed].append(st)

    ans = 0
    visit = [False] * (n + 1)
    for i in range(1, n + 1):
        if visit[i]: continue
        ans += dfs_tree_checker(i)

    if ans > 1: print(f'Case {idx}: A forest of {ans} trees.')
    elif ans == 1: print(f'Case {idx}: There is one tree.')
    else: print(f'Case {idx}: No trees.')