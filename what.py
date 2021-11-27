import sys
import math
input = sys.stdin.readline
X = 1000000007


def getExpectedValue(n, s):
    return s * getSquaredNumber(n, X-2) % X


def getSquaredNumber(num, exp):
    if exp == 1:
        return num

    if exp % 2 == 0:
        half = getSquaredNumber(num, exp//2)
        return half * half % X
    else:
        return num * getSquaredNumber(num, exp - 1) % X


if __name__ == '__main__':
    M = int(input())

    sum = 0
    for _ in range(M):
        n, s = map(int, input().split())
        gcd = math.gcd(n, s)
        n //= gcd
        s //= gcd

        sum += getExpectedValue(n, s)
        sum %= X

    print(sum)