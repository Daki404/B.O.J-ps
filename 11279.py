import sys
input = sys.stdin.readline

class Max_heap:
    def __init__(self):
        self.queue = [0]

    def insert(self, a):
        self.queue.append(a)
        last_idx = len(self.queue) - 1
        while last_idx > 1:
            parent_idx = last_idx // 2
            if self.queue[parent_idx] < self.queue[last_idx]:
                self.queue[parent_idx], self.queue[last_idx] = self.queue[last_idx], self.queue[parent_idx]
            else:
                break
            last_idx = parent_idx

    def delete(self):
        if len(self.queue) <= 1:
            print(0)
            return
        self.queue[1], self.queue[-1] = self.queue[-1], self.queue[1]
        print(self.queue.pop())
        self.heap(1)

    def heap(self, st):
        left_idx, right_idx = st * 2, st * 2 + 1
        if left_idx > len(self.queue) - 1: return
        try:
            if self.queue[left_idx] > self.queue[right_idx]:
                    if self.queue[left_idx] > self.queue[st]:
                        self.queue[left_idx], self.queue[st] = self.queue[st], self.queue[left_idx]
                        self.heap(left_idx)
            else:
                if self.queue[right_idx] > self.queue[st]:
                    self.queue[st], self.queue[right_idx] = self.queue[right_idx], self.queue[st]
                    self.heap(right_idx)
        except:
            if self.queue[left_idx] > self.queue[st]:
                self.queue[left_idx], self.queue[st] = self.queue[st], self.queue[left_idx]
                self.heap(left_idx)


heap = Max_heap()

for _ in range(int(input())):
    n = int(input())
    if n:
        heap.insert(n)
    else:
        heap.delete()