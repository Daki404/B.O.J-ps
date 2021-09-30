import sys
input = sys.stdin.readline

aim_ch = int(input())

n = int(input())
btn = {str(i) : True for i in range(0, 10)}
error_btn = list(map(int, input().split()))

for i in error_btn:
    btn[str(i)] = False

ans = abs(aim_ch - 100)

for i in range(1000001):
    num = str(i)
    for j in num:
        if not btn[j]: break
    else:
        ans = min(ans, abs(i - aim_ch) + len(num))

print(ans)