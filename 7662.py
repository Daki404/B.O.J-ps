import heapq, sys
input = sys.stdin.readline

for _ in range(int(input())):
    max_heap = []
    min_heap = []
    remove_num = [False] * 1000001

    for i in range(int(input())):
        a, b = input().strip().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(max_heap, (-b, i))
            heapq.heappush(min_heap, (b, i))
        else:
            if b == 1:
                if max_heap:
                    tmp = heapq.heappop(max_heap)[1]
                    while max_heap and remove_num[tmp]:
                        tmp = heapq.heappop(max_heap)[1]
                    remove_num[tmp] = True
            else:
                if min_heap:
                    tmp = heapq.heappop(min_heap)[1]
                    while min_heap and remove_num[tmp]:
                        tmp = heapq.heappop(min_heap)[1]
                    remove_num[tmp] = True

    while min_heap and remove_num[min_heap[0][1]]:
        heapq.heappop(min_heap)

    while max_heap and remove_num[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')