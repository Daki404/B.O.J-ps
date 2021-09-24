import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bug = {}
ans = []

for _ in range(n):
    bug[input().strip()] = True
for _ in range(m):
    if (tmp := input().strip()) in bug: ans.append(tmp)

print(len(ans))
for i in sorted(ans):
    print(i)