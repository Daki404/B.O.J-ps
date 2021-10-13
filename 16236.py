from collections import deque
import sys, heapq

input = sys.stdin.readline
dx, dy = [0, -1, 1, 0], [-1, 0, 0, 1]


def shark_finder(sea):
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                sea[i][j] = 2
                return i, j
    return None


def bfs_hunt(st_x, st_y, dis):
    visit = [[False] * n for _ in range(n)]
    visit[st_y][st_x] = True
    queue = deque([[dis, st_y, st_x]])
    hunt_range = [[sys.maxsize, 0, 0]]

    while queue:
        dis, y, x = queue.popleft()
        if dis > hunt_range[0][0]: continue
        for i in range(4):
            n_x, n_y = x + dx[i], y + dy[i]
            if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n: continue
            if visit[n_y][n_x] or (new := sea[n_y][n_x]) > (now := sea[st_y][st_x]): continue
            visit[n_y][n_x] = True
            queue.append([dis + 1, n_y, n_x])
            if 0 < new < now: heapq.heappush(hunt_range, [dis + 1, n_y, n_x])
    if len(hunt_range) > 1: return hunt_range[0]
    return None


n = int(input())

sea = []
for _ in range(n):
    sea.append(list(map(int, input().split())))

ans = 0
size = feed = 2
y, x = shark_finder(sea)

while True:
    hunt = bfs_hunt(x, y, 0)
    if hunt is None:
        print(ans)
        break

    dis, h_y, h_x = hunt
    ans += dis

    feed -= 1
    if feed == 0:
        size += 1
        feed = size
    sea[h_y][h_x] = size
    sea[y][x] = 0
    x, y = h_x, h_y