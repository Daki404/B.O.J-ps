import sys
input = sys.stdin.readline

N, R, C = map(int, input().split())


def sol(row, col, R, C, ans=0):
    if row == R and col == C: return ans
    h_row, h_col = row // 2, col // 2
    one_block = h_row * h_col
    if R < h_row:
        if C < h_col:  # 1사분면
            return sol(h_row, h_col, R, C, ans)
        else:  # 2사분면
            return sol(h_row, h_col, R, C - h_col, ans + one_block)
    else:
        if C < h_col:  # 3사분면
            return sol(h_row, h_col, R - h_row, C, ans + one_block * 2)
        else:  # 4사분면
            return sol(h_row, h_col, R - h_row, C - h_col, ans + one_block * 3)


print(sol(2**N, 2**N, R, C))