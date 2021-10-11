from collections import deque
from itertools import islice
import sys
input = sys.stdin.readline


def bfs_block(x, y, cnt=4, tmp=0):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    ans = 0
    visit = [[False] * col for _ in range(row)]
    queue = deque([(x, y, cnt, tmp)])

    while queue:
        x, y, cnt, tmp = queue.popleft()
        if cnt == 0:
            ans = max(ans, tmp)
            continue
        visit[y][x] = True
        add = 0
        for i in range(4):
            v_x = x + dx[i]
            v_y = y + dy[i]
            if 0 <= v_x < col and 0 <= v_y < row and not visit[v_y][v_x]:
                queue.append((v_x, v_y, cnt - 1, tmp + field[v_y][v_x]))
                add += 1
        if add >= 3:
            num = sorted([i[2] for i in islice(queue, len(queue) - 3, len(queue))])
            ans = max(ans, sum(num[:3]) - (2 * field[y][x]))
    return ans


row, col = map(int, input().split())
field = []

for _ in range(row):
    field.append(list(map(int, input().split())))

ans = 0
for r in range(row):
    for j in range(col):
        ans = max(ans, bfs_block(j, r))
print(ans)
