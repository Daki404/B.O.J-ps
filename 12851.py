from collections import deque
import sys
input = sys.stdin.readline

st, ed = map(int, input().split())


def bfs(st, ed):
    visit = [-1] * 100001
    cnt = [0] * 100001
    visit[st], cnt[st] = 0, 1
    queue = deque([st])

    while queue:
        v = queue.popleft()
        for i in (1, -1, v):
            new_v = v + i
            if 0 > new_v or new_v > 100000: continue
            if visit[new_v] == - 1:
                visit[new_v] = visit[v] + 1
                cnt[new_v] = cnt[v]
                queue.append(new_v)
            elif visit[new_v] == visit[v] + 1:
                cnt[new_v] += cnt[v]
    return visit[ed], cnt[ed]


print(*bfs(st, ed), sep='\n')
