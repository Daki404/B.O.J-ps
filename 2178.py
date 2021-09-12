from collections import deque
import sys
input = sys.stdin.readline

field = []
N, M = map(int, input().split())
for _ in range(N):
    tmp = list(map(int, list(input().strip())))
    field.append(tmp)


def escape(x, y):
    queue = deque([(x, y)])
    field[0][0] = 2
    while queue:
        x, y = queue.popleft()
        if x == M - 1 and y == N - 1: return field[y][x] - 1
        for i, j in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            new_x, new_y = x + i, y + j
            if 0 <= new_x < M and 0 <= new_y < N and field[new_y][new_x] == 1:
                field[new_y][new_x] = field[y][x] + 1
                queue.append((new_x, new_y))


print(escape(0, 0))