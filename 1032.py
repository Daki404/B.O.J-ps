import sys
input = sys.stdin.readline

line = [input().strip() for _ in range(int(input()))]
ans = []

for i in range(len(line[0])):
    for j in range(1, len(line)):
        if line[j][i] != line[j - 1][i]:
            ans.append('?')
            break
    else:
        ans.append(line[0][i])

print(''.join(ans))
