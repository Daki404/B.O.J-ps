from math import pow, sqrt
import sys
input = sys.stdin.readline


def star_distance(a, b):
    return round(sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)), 3)


def find(a):
    while a != parent[a]:
        a = parent[a]
    return a


def union(a, b):
    a, b = find(a), find(b)
    if a <= b: parent[a] = b
    else: parent[b] = a


star_num = int(input())
stars = [list(map(float, input().split())) for _ in range(star_num)]

parent = list(range(star_num))

roads = []
for i in range(star_num - 1):
    for j in range(i + 1, star_num):
        roads.append([i, j, star_distance(stars[i], stars[j])])

roads.sort(key=lambda x: x[2])

ans = 0
for i in roads:
    st, ed, cost = i
    if find(st) == find(ed): continue
    union(st, ed)
    ans += cost
print(round(ans, 3))