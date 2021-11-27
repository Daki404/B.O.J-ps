from itertools import combinations
import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    vector = []
    total_x = total_y = 0
    ans = float('inf')

    for _ in range(int(input())):
        x, y = map(int, input().split())
        total_x += x
        total_y += y
        vector.append((x, y))

    combi = list(combinations(vector, len(vector) // 2))

    for i in combi[:len(combi) // 2]:
        x_tmp = y_tmp = 0

        for x, y in i:
            x_tmp += x
            y_tmp += y

        x = total_x - x_tmp
        y = total_y - y_tmp

        ans = min(ans, ((x - x_tmp) ** 2 + (y - y_tmp) ** 2) ** 0.5)
    print(f'{ans:.12f}')

