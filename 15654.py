import sys
input = sys.stdin.readline


def permutation(arr, n):
    arr = sorted(arr)
    used = [False for _ in range(len(arr))]
    result = []

    def gerenerate(chosen, used):
        if len(chosen) == n:
            result.append(chosen[:])
            return
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = True
                gerenerate(chosen, used)
                used[i] = False
                chosen.pop()
    gerenerate([], used)
    return result


n, m = map(int, input().split())
line = list(map(int, input().split()))
ans = permutation(line, m)
for i in ans:
    print(*i)


