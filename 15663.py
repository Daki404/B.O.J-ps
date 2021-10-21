from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
line = list(map(int, input().split()))


def num_deleter(arr, m):
    counter = defaultdict(int)
    for i in arr:
        counter[i] += 1
    for i, j in counter.items():
        if j > m:
            counter[i] = m
    result = []
    for i in counter:
        for _ in range(counter[i]):
            result.append(i)
    return result


def permutation(arr, n):
    arr = sorted(arr)
    for i in range(len(arr)):
        if n == 1: yield [arr[i]]
        else:
            for next in permutation(arr[:i] + arr[i + 1:], n - 1):
                yield [arr[i]] + next


line = num_deleter(line, m)
for result in permutation(line, m):
    print(*result)