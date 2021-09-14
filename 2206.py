from collections import deque
import sys, copy
input = sys.stdin.readline


def sol(x=0, y=0, z=0):
    field[0][0][0] = 2
    queue = deque([(x, y, z)])
    while queue:
        x, y, z = queue.popleft()
        for i, j in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            new_x, new_y = x + i, y + j
            if 0 <= new_x < w and 0 <= new_y < h:
                if (now := field[z][new_y][new_x]) == 0:
                    field[z][new_y][new_x] = field[z][y][x] + 1
                    queue.append((new_x, new_y, z))
                elif now == 1 and z == 0:
                    field[1][new_y][new_x] = field[0][y][x] + 1
                    queue.append((new_x, new_y, 1))
    a, b = field[0][h-1][w-1], field[1][h-1][w-1]
    if a == 0 or b == 0: return max(a, b) - 1
    return min(a, b) - 1


h, w = map(int, input().split())
field = []
for i in range(h):
    field.append(list(map(int, list(input().strip()))))
field = [field, copy.deepcopy(field)]
print(sol())