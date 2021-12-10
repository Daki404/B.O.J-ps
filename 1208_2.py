from collections import Counter
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

front = n // 2
rear = n - front

front_sum, rear_sum = [0] * (1 << front), [0] * (1 << rear)

for i in range(1 << front):
    for j in range(front):
        if i & (1 << j) > 0:
            front_sum[i] += arr[j]

for i in range(1 << rear):
    for j in range(rear):
        if i & (1 << j) > 0:
            rear_sum[i] += arr[j + front]

front_sum = Counter(front_sum)
rear_sum = Counter(rear_sum)

front_sum[0] -= 1
rear_sum[0] -= 1
ans = front_sum.get(s, 0) + rear_sum.get(s, 0)

for i in front_sum:
    if s - i in rear_sum:
        ans += front_sum[i] * rear_sum[s - i]

print(ans)