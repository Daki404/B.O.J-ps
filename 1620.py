import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_to_poketmon = {}
poketmon_to_num = {}

for i in range(n):
    name = input().strip()
    num_to_poketmon[str(i + 1)] = name
    poketmon_to_num[name] = i + 1

for _ in range(m):
    tmp = input().strip()
    if tmp.isdigit(): print(num_to_poketmon[tmp])
    else: print(poketmon_to_num[tmp])
