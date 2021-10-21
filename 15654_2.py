import sys
input = sys.stdin.readline

n, m = map(int, input().split())
line = list(map(int, input().split()))


def permutation(arr, n):
    arr = sorted(arr)
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i] + arr[i + 1:], n - 1):
                yield [arr[i]] + next


ans = permutation(line, m)
for i in ans:
    print(*i)