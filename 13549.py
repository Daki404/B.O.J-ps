from collections import deque
import sys
input = sys.stdin.readline


def bfs(n, k):
    visit = [None] * 100001
    visit[n] = 0
    queue = deque([n])

    while queue:
        v = queue.popleft()
        if v == k: return visit[v]

        if 0 < 2 * v <= 100000 and visit[2 * v] is None:
            visit[2 * v] = visit[v]
            queue.appendleft(2 * v)

        if v < 100000 and visit[v + 1] is None:
            visit[v + 1] = visit[v] + 1
            queue.append(v + 1)

        if v > 0 and visit[v - 1] is None:
            visit[v - 1] = visit[v] + 1
            queue.append(v - 1)


n, k = map(int, input().split())
print(bfs(n, k))

