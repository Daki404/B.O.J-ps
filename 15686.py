from itertools import combinations
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
field = []
house, chicken = [], []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:  # house
            house.append((i, j))
        elif line[j] == 2:  # chicken shop
            chicken.append((i, j))
    field.append(line)

chicken_distance = [[None] * len(chicken) for _ in range(len(house))]

for i in range(len(chicken)):
    for j in range(len(house)):
        chicken_distance[j][i] = abs(chicken[i][0] - house[j][0]) + abs(chicken[i][1] - house[j][1])

min_distance = float('inf')
for shop in combinations(range(len(chicken)), m):
    sum_distance = 0
    for i in range(len(house)):
        tmp_distance = float('inf')
        for j in shop:
            tmp_distance = min(tmp_distance, chicken_distance[i][j])
        sum_distance += tmp_distance
    min_distance = min(min_distance, sum_distance)
print(min_distance)


