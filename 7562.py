from collections import deque
import sys

input = sys.stdin.readline
move_x = [-2, -2, -1, -1, 2, 2, 1, 1]
move_y = [1, -1, 2, -2, 1, -1, 2, -2]


def knight_calc(st, ed, field):
    queue = deque([st])
    field[st[0]][st[1]] = 1
    while queue:
        v = queue.popleft()
        if v == ed: return field[v[0]][v[1]] - 1
        for i in range(8):
            new_v = (v[0] + move_y[i]), (v[1] + move_x[i])
            if 0 <= new_v[0] < len(field) and 0 <= new_v[1] < len(field) and field[new_v[0]][new_v[1]] == 0:
                queue.append(new_v)
                field[new_v[0]][new_v[1]] = field[v[0]][v[1]] + 1
    return 0


for _ in range(int(input())):
    size = int(input())
    field = [[0] * size for _ in range(size)]
    st = tuple(map(int, input().split()))
    ed = tuple(map(int, input().split()))
    print(knight_calc(st, ed, field))