import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = []

for _ in range(n):
    line = list(map(int, input().split()))
    for i in range(1, n):
        line[i] += line[i-1]
    table.append(line)

for i in range(n):
    for j in range(1, n):
        table[j][i] += table[j - 1][i]

for _ in range(m):
    y_1, x_1, y_2, x_2 = map(int, input().split())
    x_1 -= 1
    x_2 -= 1
    y_1 -= 1
    y_2 -= 1

    ans = table[y_2][x_2]
    flag = [False, False]
    if x_1 >= 1:
        ans -= table[y_2][x_1 - 1]
        flag[0] = True
    if y_1 >= 1:
        ans -= table[y_1 - 1][x_2]
        flag[1] = True
    if flag[0] and flag[1]: ans += table[y_1 - 1][x_1 - 1]
    print(ans)


