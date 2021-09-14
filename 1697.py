from collections import deque
import sys
input = sys.stdin.readline


def sol(st, ed):
    line = [0] * 100001
    line[st] = 1
    queue = deque([st])
    while queue:
        v = queue.popleft()
        if v == ed: return line[v] - 1
        for i in (1, -1, v):
            new_v = v + i
            if 0 <= new_v <= 100000 and line[new_v] == 0:
                queue.append(new_v)
                line[new_v] = line[v] + 1


st, ed = map(int, input().split())
print(sol(st, ed))