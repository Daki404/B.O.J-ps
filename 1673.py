def sol(coupon, stamp):
    ans = coupon
    while coupon // stamp:
        ans += coupon // stamp
        coupon = coupon // stamp + coupon % stamp
    return ans


while True:
    try:
        n, k = map(int, input().split())
        print(sol(n, k))

    except EOFError:
        break