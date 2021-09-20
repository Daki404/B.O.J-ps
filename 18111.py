import sys, math
input = sys.stdin.readline

h, w, b = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(h)]


ans = [math.inf, 0]

for i in range(0, 257):
    cost, block = 0, b
    for j in range(h):
        for k in range(w):
            if (now := field[j][k]) == i: continue
            elif now > i:
                diff = now - i
                cost += 2 * diff
                block += diff
            else:
                diff = i - now
                cost += diff
                block -= diff
    if block < 0: continue
    if cost == ans[0]: ans[1] = max(i, ans[1])
    elif cost < ans[0]: ans = [cost, i]

print(*ans)