import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

ans = float('inf'), 0, 0
l_ptr, r_ptr = 0, n - 1

while l_ptr != r_ptr and l_ptr < n and r_ptr >= 0:
    mix_liquid = liquid[l_ptr] + liquid[r_ptr]
    if abs(mix_liquid) < ans[0]: ans = abs(mix_liquid), liquid[l_ptr], liquid[r_ptr]
    if mix_liquid == 0: break
    elif mix_liquid > 0: r_ptr -= 1
    else: l_ptr += 1
print(*sorted((ans[1], ans[2])))