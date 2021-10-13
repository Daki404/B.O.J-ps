import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
h_block = [[[0, 1], [0, 2], [1, 1]], [[0, 1], [0, 2], [-1, 1]], [[1, 0], [2, 0], [1, 1]], [[1, 0], [2, 0], [1, -1]]]


def dfs_block(x, y, cnt=0, num=0):
    global ans
    if cnt == 4:
        ans = max(ans, num)
        return
    for i in range(4):
        v_x, v_y = x + dx[i], y + dy[i]
        if 0 <= v_x < col and 0 <= v_y < row and not visit[v_y][v_x]:
            visit[v_y][v_x] = True
            dfs_block(v_x, v_y, cnt + 1, num + field[v_y][v_x])
            visit[v_y][v_x] = False


def star_block(x, y):
    global ans
    for i in h_block:
        num = field[y][x]
        try:
            for j in range(3):
                num += field[y + i[j][1]][x + i[j][0]]
        except IndexError:
            num = 0
        ans = max(ans, num)


row, col = map(int, input().split())
visit = [[False] * col for _ in range(row)]
field = []
ans = 0

for _ in range(row):
    field.append(list(map(int, input().split())))

for i in range(row):
    for j in range(col):
        visit[i][j] = True
        dfs_block(j, i)
        visit[i][j] = False
        star_block(j, i)
print(ans)



