import sys
input = sys.stdin.readline

n = int(input())
tmp = list(map(int, input().split()))
min_sum, max_sum = tmp[:], tmp[:]

for i in range(1, n):
    new = list(map(int, input().split()))
    max_l, max_m, max_r = max(max_sum[0], max_sum[1]), max(max_sum), max(max_sum[1], max_sum[2])
    min_l, min_m, min_r = min(min_sum[0], min_sum[1]), min(min_sum), min(min_sum[1], min_sum[2])
    max_sum = [max_l + new[0], max_m + new[1], max_r + new[2]]
    min_sum = [min_l + new[0], min_m + new[1], min_r + new[2]]
    tmp = new

print(max(max_sum), min(min_sum))
