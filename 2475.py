import sys
input = sys.stdin.readline

line = list(map(int, input().split()))
ans = 0

for i in line:
    ans += i ** 2

print(ans % 10)