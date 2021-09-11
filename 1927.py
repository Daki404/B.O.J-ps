import heapq, sys
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    n = int(input())
    if n:
        heapq.heappush(heap, (abs(n), n))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)