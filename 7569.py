from collections import deque
import sys
input = sys.stdin.readline


def tomato(field):
    pos, ans = [], 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if field[i][j][k] == 1: pos.append((k, j, i))

    def sol(pos):
        queue = deque(pos)
        while queue:
            v = queue.popleft()
            x, y, z = v[0], v[1], v[2]
            if field[z][y][x] < 1: continue
            for i, j in zip([0, 0, 1, -1], [-1, 1, 0, 0]):
                new_x, new_y = x + i, y + j
                if 0 <= new_x < M and 0 <= new_y < N and field[z][new_y][new_x] == 0:
                    field[z][new_y][new_x] = field[z][y][x] + 1
                    queue.append((new_x, new_y, z))
            for i in (1, -1):
                new_z = z + i
                if 0 <= new_z < H and field[new_z][y][x] == 0:
                    field[new_z][y][x] = field[z][y][x] + 1
                    queue.append((x, y, new_z))
        ans = 0
        for i in field:
            for j in i:
                for k in j:
                    if k == 0: return -1
                    ans = max(ans, k)
        return ans - 1
    return sol(pos)


M, N, H = map(int, input().split())
field = []
for _ in range(H):
    tmp_field = []
    for _ in range(N):
        tmp_field.append(list(map(int, input().split())))
    field.append(tmp_field)

print(tomato(field))