from math import *
import sys

input = sys.stdin.readline


class Segement:
    def __init__(self, a):
        self.a = a
        self.tree_depth = ceil(log(len(self.a), 2) + 1)
        self.tree = [0] * (2 ** self.tree_depth)

        def make_tree(node, st, ed):
            if st == ed:
                self.tree[node] = self.a[st]
            else:
                mid = (st + ed) // 2
                left = make_tree(node * 2, st, mid)
                right = make_tree(node * 2 + 1, mid + 1, ed)
                self.tree[node] = left + right
            return self.tree[node]
        make_tree(1, 0, len(self.a) - 1)

    def sum(self, left, right):
        left -= 1
        right -= 1

        def sum_tree(node, st, ed):
            if ed < left or right < st: return 0
            elif left <= st and ed <= right:
                return self.tree[node]
            mid = (st + ed) // 2
            return sum_tree(node * 2, st, mid) + sum_tree(node * 2 + 1, mid + 1, ed)
        return sum_tree(1, 0, len(self.a) - 1)

    def update(self, idx, num):
        idx -= 1
        diff = num - self.a[idx]
        self.a[idx] = num

        def update_tree(node, st, ed):
            if idx < st or ed < idx: return
            self.tree[node] += diff
            if st != ed:
                mid = (st + ed) // 2
                update_tree(node * 2, st, mid)
                update_tree(node * 2 + 1, mid + 1, ed)

        update_tree(1, 0, len(self.a) - 1)


a = []
n, k, m = map(int, input().split())  # 수의 개수, 구간 합의 수, 변경 횟수

for i in range(n):
    a.append(int(input()))

segement_tree = Segement(a)

for i in range(k + m):
    a, b, c = map(int, input().split())  # a == 1; b번째 수를 c로, a == 2; b ~ c 구간의 합
    if a == 1:
        segement_tree.update(b, c)
    else:
        print(segement_tree.sum(b, c))