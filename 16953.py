from collections import deque
import sys
input = sys.stdin.readline


def bfs(st, ed):
    queue = deque([[st, 1]])

    while queue:
        v, cnt = queue.popleft()
        if v == ed: return cnt
        if (new := 2 * v) <= ed:
            queue.append([new, cnt + 1])
        if (new := 10 * v + 1) <= ed:
            queue.append([new, cnt + 1])
            queue.append([new, cnt + 1])
    return -1


a, b = map(int, input().split())
print(bfs(a, b))
