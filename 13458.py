import sys, math
input = sys.stdin.readline

n = int(input())
classroom = list(map(int, input().split()))
major, minor = map(int, input().split())
ans = n

for i in range(n):
    if classroom[i] <= major: continue
    classroom[i] -= major
    ans += math.ceil(classroom[i] / minor)

print(ans)