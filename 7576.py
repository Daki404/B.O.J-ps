from collections import deque
import sys
input = sys.stdin.readline


def tomato(pos: list):
    queue = deque(pos)
    while queue:
        x, y = queue.popleft()
        if field[y][x] <= 0: continue
        for i, j in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            new_x, new_y = x + i, y + j
            if 0 <= new_x < M and 0 <= new_y < N and field[new_y][new_x] == 0:
                field[new_y][new_x] = field[y][x] + 1
                queue.append((new_x, new_y))
    ans = 0
    for i in field:
        for j in i:
            if j == 0: return -1
            ans = max(ans, j)
    return ans - 1


field, pos = [], []
M, N = map(int, input().split())
for _ in range(N):
    field.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            pos.append((j, i))

print(tomato(pos))