import sys
input = sys.stdin.readline

n, m = map(int, input().split())
line = list(map(int, input().split()))


def permutation_repeat(arr, n):
    arr = sorted(arr)

    for i in range(len(arr)):
        if n == 1: yield [arr[i]]
        else:
            for next in permutation_repeat(arr[i:], n - 1):
                yield [arr[i]] + next


for result in permutation_repeat(line, m):
    print(*result)