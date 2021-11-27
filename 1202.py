import sys, heapq
input = sys.stdin.readline


jewel_num, bag_num = map(int, input().split())
jewels = []
for _ in range(jewel_num):
    heapq.heappush(jewels, list(map(int, input().split())))
bags = [int(input()) for _ in range(bag_num)]

jewels.sort()
bags.sort()

ans = 0
possible = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(possible, -heapq.heappop(jewels)[1])
    if possible:
        ans -= heapq.heappop(possible)
    elif not jewels:break
print(ans)




print(ans)