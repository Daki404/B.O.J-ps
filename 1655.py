import heapq, sys
input = sys.stdin.readline

small_heap, big_heap  = [], []

n = int(input())
median = int(input())
print(median)

for i in range(n - 1):
    tmp = int(input())
    if tmp < median:
        heapq.heappush(small_heap, (-tmp, tmp))
        if len(small_heap) != len(big_heap):
            heapq.heappush(big_heap, median)
            median = heapq.heappop(small_heap)[1]
    else:
        heapq.heappush(big_heap, tmp)
        if len(small_heap) != len(big_heap):
            heapq.heappush(small_heap, (-median, median))
            median = heapq.heappop(big_heap)
    if i % 2 == 0: # median과 small_heap 중 작은 값
        if len(small_heap) > len(big_heap):
            print(min(median, small_heap[0][1]))
        else:
            print(min(median, big_heap[0]))
    else:
        print(median)