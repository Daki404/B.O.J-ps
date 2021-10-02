from collections import deque, defaultdict
import sys

input = sys.stdin.readline
friend = defaultdict(list)

n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

kevin_bacon = [0] * n


for i in range(1, n + 1):
    queue = deque([(i, 0)])
    visit_cnt = [sys.maxsize] * (n + 1)
    visit = [False] * (n + 1)

    while queue:
        val, att = queue.popleft()
        visit[val] = True
        visit_cnt[val] = min(visit_cnt[val], att)

        for k in friend[val]:
            if not visit[k]:
                queue.append((k, att + 1))
            else:
                visit_cnt[k] = min(visit_cnt[k], att)
    kevin_bacon[i - 1] = sum(visit_cnt[1:])

min_bacon = min(kevin_bacon)

for i in range(n):
    if kevin_bacon[i] == min_bacon:
        print(i + 1)
        break

