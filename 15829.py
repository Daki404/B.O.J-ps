import sys
input = sys.stdin.readline

n = int(input())
line = input().strip()
ans = 0

for i, j in enumerate(line):
    ans += (ord(j) - 96) * 31 ** i

print(ans % 1234567891)
