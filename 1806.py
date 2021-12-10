import sys
input = sys.stdin.readline

n, s = map(int, input().split())
line = list(map(int, input().split()))


def sol():
    ans = n + 1
    l_ptr, r_ptr = 0, 0
    tmp_sum = line[0]

    while 0 <= l_ptr and l_ptr <= r_ptr and r_ptr < n:
        if tmp_sum >= s:
            ans = min(ans, r_ptr - l_ptr + 1)
            tmp_sum -= line[l_ptr]
            l_ptr += 1
        else:
            r_ptr += 1
            if r_ptr < n: tmp_sum += line[r_ptr]

    if ans == (n + 1): return 0
    else: return ans

print(sol())