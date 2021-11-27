from collections import deque
import sys
input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
queue = deque([])


def spread(x, y):
    tmp = field[y][x] // 5
    for i in range(4):
        v_x, v_y = x + dx[i], y + dy[i]
        if 0 <= v_x < c and 0 <= v_y < r and field[v_y][v_x] != -1:
            field[y][x] -= tmp
            queue.append([v_x, v_y, tmp])


def air_purify(y1, y2):
    field[y1 - 1][0], field[y2 + 1][0] = 0, 0
    for i in range(y1 - 1, 0, -1):
        field[i][0], field[i - 1][0] = field[i - 1][0], field[i][0]
    for i in range(y2 + 1, r - 1):
        field[i][0], field[i + 1][0] = field[i + 1][0], field[i][0]

    for i in range(c - 1):
        field[0][i], field[0][i + 1] = field[0][i + 1], field[0][i]
        field[r - 1][i], field[r - 1][i + 1] = field[r - 1][i + 1], field[r - 1][i]

    for i in range(y1):
        field[i][c - 1], field[i + 1][c - 1] = field[i + 1][c - 1], field[i][c - 1]
    for i in range(r - 1, y2, -1):
        field[i][c - 1], field[i - 1][c - 1] = field[i - 1][c - 1], field[i][c - 1]

    for i in range(c - 1, 1, -1):
        field[y1][i], field[y1][i - 1] = field[y1][i - 1], field[y1][i]
        field[y2][i], field[y2][i - 1] = field[y2][i - 1], field[y2][i]


r, c, t = map(int, input().split())

field = []
y1 = y2 = 0
for i in range(r):
    line = list(map(int, input().split()))
    if line[0] == -1:
        if y1: y2 = i
        else: y1 = i
    field.append(line)

for _ in range(t):
    for i in range(r):
        for j in range(c):
            if field[i][j] > 0: spread(j, i)
    while queue:
        x, y, dust = queue.popleft()
        field[y][x] += dust
    air_purify(y1, y2)

ans = sum([sum(i) for i in field]) + 2
print(ans)