from collections import deque, defaultdict
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    buliding_num, bulid_num = map(int, input().split())
    line = list(map(int, input().split()))
    cost = {i + 1: j for i, j in enumerate(line)}

    enter = [0] * (buliding_num + 1)
    dp = [0] * (buliding_num + 1)

    bulid = defaultdict(list)
    for _ in range(bulid_num):
        st, ed = map(int, input().split())
        bulid[st].append(ed)
        enter[ed] += 1

    destination = int(input())

    queue = deque()
    for i in range(1, len(enter)):
        if enter[i] == 0:
            queue.append(i)
            dp[i] = cost[i]

    while queue:
        v = queue.popleft()
        if v == destination: break
        for i in bulid[v]:
            enter[i] -= 1
            dp[i] = max(dp[i], cost[i] + dp[v])
            if enter[i] == 0: queue.append(i)
    print(dp[destination])