import sys
input = sys.stdin.readline

n = int(input())

field = [list(map(int, input().split())) for _ in range(n - 1)]
field = list(map(int, input().split())) + field