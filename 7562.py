from collections import deque
import sys
input = sys.stdin.readline


def knight_calc(v, ed, w):
    if v == ed: return 0
    queue = deque([st])
    visit = []
    while queue:
        v = queue.popleft()
        if v in visit: continue
        visit.append(v)
        if st == ed: return (len(visit) - 1) // 8 + 1
        if (0 <= v[0] and v[0] < w) and (0 <= v[1] and v[1] < w):
            queue.append((v[0] - 2, v[1] - 1))
            queue.append((v[0] - 2, v[1] + 1))
            queue.append((v[0] - 1, v[1] + 2))
            queue.append((v[0] - 1, v[1] - 2))

            queue.append((v[0] + 2, v[1] - 1))
            queue.append((v[0] + 2, v[1] + 1))
            queue.append((v[0] + 1, v[1] + 2))
            queue.append((v[0] + 1, v[1] - 2))


for _ in range(int(input())):
    w = int(input())
    st = tuple(map(int, input().split()))
    ed = tuple(map(int, input().split()))
    print(knight_calc(st, ed, w))