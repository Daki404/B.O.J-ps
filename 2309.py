from itertools import combinations

line = [int(input()) for _ in range(9)]
line.sort()

combi = combinations(line, 7)

for i in combi:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break