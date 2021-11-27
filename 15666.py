import sys
input = sys.stdin.readline


def solve(line, m):
    for i in range(len(line)):
        if m == 1: yield [line[i]]
        else:
            for next in solve(line[i:], m - 1):
                yield [line[i]] + next


n, m = map(int, input().split())
line = sorted(set(map(int, input().split())))


for i in solve(line, m):
    print(*i)