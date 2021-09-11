import sys, math

input = sys.stdin.readline


def segment_tree(a):
    tree_depth = math.ceil(math.log(len(a), 2) + 1)
    tree = [None] * (2 ** tree_depth)

    def make_tree(node, st, ed):
        if st == ed:
            tree[node] = (a[st], a[st])
        else:
            md = (st + ed) // 2
            left = make_tree(node * 2, st, md)
            right = make_tree(node * 2 + 1, md + 1, ed)
            tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
        return tree[node]
    make_tree(1, 0, len(a) - 1)
    return tree


def min_max(arr: list, tree: list, a: int, b: int) -> tuple:
    a -= 1
    b -= 1

    def find(node, st, ed):
        if a <= st and ed <= b: return tree[node]
        elif a > ed or b < st: return math.inf, 0
        else:
            md = (st + ed) // 2
            left = find(node * 2, st, md)
            right = find(node * 2 + 1, md + 1, ed)
            return min(left[0], right[0]), max(left[1], right[1])
    return find(1, 0, len(arr) - 1)


arr = []
N, M = map(int, input().split())

for _ in range(N):
    arr.append(int(input()))

tree = segment_tree(arr)

for _ in range(M):
    a, b = map(int, input().split())
    print(* min_max(arr, tree, a, b))