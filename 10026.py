import sys
input = sys.stdin.readline


def dfs(pic: list, color: dict, ans=0) -> int:
    n = len(pic)
    visit = [[False] * n for _ in range(n)]
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                stack = [(j, i)]
                ans += 1
                while stack:
                    v_x, v_y = stack.pop()
                    visit[v_y][v_x] = True
                    for k in range(4):
                        x, y = v_x + dx[k], v_y + dy[k]
                        if 0 <= x < n and 0 <= y < n and not visit[y][x]:
                            if color[pic[v_y][v_x]] == color[pic[y][x]]:
                                stack.append((x, y))
    return ans


n = int(input())
picture = []

for _ in range(n):
    picture.append(list(input().strip()))

print(dfs(picture, {'R': 'r', 'G': 'g', 'B': 'b'}), dfs(picture, {'R': 'r-g', 'G': 'r-g', 'B': 'b'}))
