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

front_sum.sort(reverse=True)
rear_sum.sort()

ans = 0
l_arr, r_arr = 1 << front, 1 << rear
l_pt = r_pt = 0
while l_pt < l_arr and r_pt < r_arr:
    sum_tmp = front_sum[l_pt] + rear_sum[r_pt]
    if sum_tmp == s:
        l_cnt = r_cnt = 1
        l_pt += 1
        r_pt += 1

        while l_pt < l_arr and front_sum[l_pt] == front_sum[l_pt - 1]:
            l_cnt += 1
            l_pt += 1
        while r_pt < r_arr and rear_sum[r_pt] == rear_sum[r_pt - 1]:
            r_cnt += 1
            r_pt += 1
        ans += l_cnt * r_cnt
    elif sum_tmp > s:
        l_pt += 1
    else:
        r_pt += 1

print(ans if s != 0 else ans - 1)