import sys
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    x, y, a, b = map(int, input().split())
    end_year = x * y // gcd(x, y)

    possible_a, possible_b = set(), set()

    for i in range(a, end_year + 1, x):
        possible_a.add(i)

    for i in range(b, end_year + 1, y):
        possible_b.add(i)

    if (ans := possible_a & possible_b):
        print(*ans)
    else: print(-1)