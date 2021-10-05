from collections import deque
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    a, b = map(int, input().split())
    visit = [False] * 10000
    visit[a] = True
    queue = deque([[a, '']])
    while queue:
        num, log = queue.popleft()
        if num == b:
            print(log)
            break
        idx = 2 * num % 10000
        if not visit[idx]:
            queue.append([idx, log + 'D'])
            visit[idx] = True
        idx = num - 1
        if not visit[idx]:
            if idx == 0: idx = 9999
            queue.append([idx, log + 'S'])
            visit[idx] = True
        idx = num % 1000 * 10 + num // 1000
        if not visit[idx]:
            queue.append([idx, log + 'L'])
            visit[idx] = True
        idx = num % 10 * 1000 + num // 10
        if not visit[idx]:
            queue.append([idx, log + 'R'])
            visit[idx] = True

