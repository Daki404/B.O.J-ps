import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dp_map(x, y, ans=0):
    if (tmp := dp[y][x]) != -1: return tmp
    dp[y][x] = 0
    for i, j in zip([0, 0, -1, 1], [1, -1, 0, 0]):
        new_x, new_y = x + i, y + j
        if 0 <= new_x < w and 0 <= new_y < h and field[y][x] < field[new_y][new_x]:
            dp[y][x] += dp_map(new_x, new_y)
    return dp[y][x]


h, w = map(int, input().split())
field = []
dp = [[-1] * w for _ in range(h)]
dp[0][0] = 1

for _ in range(h):
    field.append(list(map(int, input().split())))
print(dp_map(w-1, h-1))
