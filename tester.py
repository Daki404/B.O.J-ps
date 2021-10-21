import sys
input = sys.stdin.readline

def permutation(arr, n):
    arr = sorted(arr)
    log = 0
    for i in range(len(arr)):
        if log == arr[i]: continue
        log = arr[i]
        if n == 1: yield [arr[i]]
        else:
            for next in permutation(arr[:i] + arr[i+1:], n-1):
                yield [arr[i]] + next

n, m = map(int, input().split())
line = list(map(int, input().split()))

for result in permutation(line, m):
    print(*result)