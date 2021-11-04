import sys
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


def cheese_dfs():
    ans = 0

    def dfs(x, y, field):
        visit = [[0] * m for _ in range(n)]
        visit[y][x] = -1
        stack = [(x, y)]
        melt = False

        while stack:
            x, y = stack.pop()
            for i in range(4):
                v_x = x + dx[i]
                v_y = y + dy[i]

                if v_x < 0 or v_x >= m or v_y < 0 or v_y >= n or visit[v_y][v_x] == -1: continue
                if field[v_y][v_x] == 1:
                    visit[v_y][v_x] += 1
                    if visit[v_y][v_x] >= 2:
                        visit[v_y][v_x] = -1
                        field[v_y][v_x] = 0
                        melt = True
                else:
                    visit[v_y][v_x] = -1
                    stack.append((v_x, v_y))
        return melt

    while True:
        if (cheese_melt := dfs(0, 0, field)): ans += cheese_melt
        else: return ans


n, m = map(int, input().split())
field = []

for _ in range(n):
    field.append(list(map(int, input().split())))

print(cheese_dfs())

