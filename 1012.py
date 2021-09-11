import sys
input = sys.stdin.readline


def sol(v: tuple, bug, visit=[]) -> int:
    if field[v[0]][v[1]] == 0: return visit, bug
    if v in visit: return visit, bug
    stack = [v]
    bug += 1
    while stack:
        v = stack.pop()
        if field[v[0]][v[1]] == 0: continue
        visit.append(v)
        if v[0] != 0 and (v[0] - 1, v[1]) not in visit: stack.append((v[0] - 1, v[1]))
        if v[0] != H - 1 and (v[0] + 1, v[1]) not in visit: stack.append((v[0] + 1, v[1]))
        if v[1] != 0 and (v[0], v[1] - 1) not in visit: stack.append((v[0], v[1] - 1))
        if v[1] != W - 1 and (v[0], v[1] + 1) not in visit: stack.append((v[0], v[1] + 1))
    return visit, bug


for _ in range(int(input())):
    W, H, K = map(int, input().split())
    field = [[0] * W for _ in range(H)]
    for _ in range(K):
        w, h = map(int, input().split())
        field[h][w] = 1

    bug, visit = 0, []
    for i in range(H):
        for j in range(W):
            visit, bug = sol((i, j), bug, visit)

    print(bug)
