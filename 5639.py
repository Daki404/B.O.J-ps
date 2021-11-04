import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def bigger_num_idx(a, b):
    for i in range(a + 1, b + 1):
        if line[i] > line[a]: return i
    return 0


def in_to_postorder(line, st=0, ed=None):
    if ed is None: ed = len(line) - 1
    post_order = []

    def make_tree(st, ed):
        if st > ed: return None
        if st == ed: return Tree(line[st])
        tmp = Tree(line[st])
        branch = bigger_num_idx(st, ed)

        if branch:
            tmp.left = make_tree(st + 1, branch - 1)
            tmp.right = make_tree(branch, ed)
        else:
            tmp.left = make_tree(st + 1, ed)
        return tmp
    tree = make_tree(st, ed)

    def postorder(tree):
        if tree is None: return
        postorder(tree.left)
        postorder(tree.right)
        post_order.append(tree.data)
    postorder(tree)

    return post_order


line = list()
while True:
    try:
        line.append(int(input()))
    except:
        break

for i in in_to_postorder(line):
    print(i)