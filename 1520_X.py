from collections import namedtuple
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
field = []
ans = [0] * (w * h)

for _ in range(h):
    tmp = list(map(int, input().split()))
    field.append(tmp)

direction = namedtuple('route', ['up', 'down', 'left', 'right'])


def sol(idx: tuple, sum: int) -> int:
    route = direction(True, True, True, True)
    if idx[0] == 0 or field[idx[0]-1][idx[1]] < field[idx[0]][idx[1]]: route = route._replace(up=False)
    if idx[0] == h - 1 or field[idx[0]+1][idx[1]] < field[idx[0]][idx[1]]: route = route._replace(down=False)
    if idx[1] == 0 or field[idx[0]][idx[1]-1] < field[idx[0]][idx[1]]: route = route._replace(left=False)
    if idx[1] == w - 1 or field[idx[0]][idx[1]+1] < field[idx[0]][idx[1]]: route = route._replace(right=False)

    ans = 0
    if route.up: ans += sol((idx[0]-1, idx[1]), sum)
    if route.down: ans += sol((idx[0]+1, idx[1]), sum)
    if route.left: ans += sol((idx[0], idx[1]-1), sum)
    if route.right: ans += sol((idx[0], idx[1]+1), sum)
    return ans


print(sol((h-1, w-1), 0))


