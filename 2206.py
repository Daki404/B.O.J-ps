from collections import deque
import sys
input = sys.stdin.readline


def sol(x=0, y=0, stave=True):
    field[0][0] = 2
    queue = deque([(x, y, stave)])
    while queue:
        x, y, stave = queue.popleft()
        if x == w - 1 and y == h - 1: return field[y][x] - 1
        for i, j in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            new_x, new_y = x + i, y + j
            if 0 <= new_x < w and 0 <= new_y < h:
                if (now := field[new_y][new_x]) == 0:
                    field[new_y][new_x] = field[y][x] + 1
                    queue.append((new_x, new_y, stave))
                elif now == 1 and stave:
                    field[new_y][new_x] = field[y][x] + 1
                    queue.append((new_x, new_y, not stave))
    return -1


h, w = map(int, input().split())
field = []
for i in range(h):
    field.append(list(map(int, list(input().strip()))))

print(sol())