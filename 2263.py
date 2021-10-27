import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def make_preorder(inorder, postorder):  # left - root - right / # left - right - root
    answer = []
    inorder_pos = [0] * (n + 1)
    for i in range(n): inorder_pos[inorder[i]] = i

    def make_tree(in_st, in_ed, post_in, post_ed):
        if in_st > in_ed or post_in > post_ed: return
        root = Node(postorder[post_ed])
        root.left = make_tree(in_st, inorder_pos[postorder[post_ed]] - 1, post_in, post_in + (inorder_pos[postorder[post_ed]] - 1 - in_st))
        root.right = make_tree(inorder_pos[postorder[post_ed]] + 1, in_ed, post_ed - 1 - (in_ed - inorder_pos[postorder[post_ed]] - 1), post_ed - 1)
        return root
    tree_root = make_tree(0, n - 1, 0, n - 1)

    def preorder(node):
        if not node: return
        nonlocal answer
        answer.append(node.data)
        preorder(node.left)
        preorder(node.right)
    preorder(tree_root)
    return answer


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

print(*make_preorder(inorder, postorder))


