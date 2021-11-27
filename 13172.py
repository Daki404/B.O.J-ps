import sys, math
input = sys.stdin.readline
mod = 1000000007


def solve(dice_poly, dice_sum):
    return dice_sum * pow(dice_poly, mod - 2, mod) % mod

ans = 0
for _ in range(int(input())):
    dice_poly, dice_sum = map(int, input().split())
    gcd = math.gcd(dice_poly, dice_sum)
    dice_poly //= gcd
    dice_sum //= gcd

    ans += solve(dice_poly, dice_sum)
    ans %= mod
print(ans)