import math, sys

input = sys.stdin.readline


class Segment:
    def __init__(self, n, a):
        self.tree_depth = math.ceil(math.log(n, 2) + 1)
        self.tree = [0] * (2 ** self.tree_depth)
        self.n = n
        self.a = a

        def make_tree(node, st, ed):
            if st == ed:
                self.tree[node] = self.a[st]
            else:
                md = (st + ed) // 2
                left = make_tree(node * 2, st, md)
                right = make_tree(node * 2 + 1, md + 1, ed)
                self.tree[node] = min(left, right)
            return self.tree[node]
        make_tree(1, 0, n - 1)

    def find(self, a, b):
        st, ed = 0, self.n - 1

        def find_tree(node, st, ed):
            if a > ed or b < st:
                return math.inf
            elif a <= st and ed <= b:
                return self.tree[node]
            else:
                md = (st + ed) // 2
                left = find_tree(node * 2, st, md)
                right = find_tree(node * 2 + 1, md + 1, ed)
                return min(left, right)
        return find_tree(1, st, ed)


def sol(n, hist):
    tree = Segment(n, hist)
    max_area = 0

    def solve(st, ed, max_area):
        if st == ed:
            return hist[st]

        min_height = tree.find(st, ed)
        width = (ed - st + 1) * min_height

        for i in range(st, ed + 1):
            if hist[i] == min_height:
                if i == st:
                    return max(width, solve(st + 1, ed, max_area))
                elif i == ed:
                    return max(width, solve(st, ed - 1, max_area))
                return max(width, solve(st, ed - 1, max_area), solve(st + 1, ed, max_area))
    return solve(0, n - 1, 0)


while True:
    n, *hist = map(int, input().split())
    if n == 0:
        break
    print(sol(n, hist))



