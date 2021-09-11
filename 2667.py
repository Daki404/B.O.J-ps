import sys
input = sys.stdin.readline

N = int(input())
house = [list(input().strip()) for _ in range(N)]
size = []
ans = 0


def dfs_house(x, y, cnt=0):
    if x < 0 or x >= N or y < 0 or y >= N: return cnt
    if house[y][x] == '0': return cnt
    house[y][x] = '0'
    cnt += 1
    for new_x, new_y in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        cnt += dfs_house(x + new_x, y + new_y)
    return cnt


for y in range(N):
    for x in range(N):
        if house[y][x] == '1':
            ans += 1
            size.append(dfs_house(x, y))

print(ans)
for i in sorted(size):
    print(i)