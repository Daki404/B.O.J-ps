import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, root):
        self.root = root

    def make_tree(self, node=None):
        if node is None: node = self.root

        def make(node):
            tmp = Node(node)
            if (left := connect[node][0]) != '.': tmp.left = make(left)
            if (right := connect[node][1]) != '.': tmp.right = make(right)
            return tmp
        self.root = make(node)

    def preorder(self, node=None):
        if node is None: node = self.root
        self.result = ''

        def order(node):
            if node is None: return ''
            self.result += node.data
            order(node.left)
            order(node.right)
        order(node)
        return self.result

    def inorder(self, node=None):
        if node is None: node = self.root
        self.result = ''

        def order(node):
            if node is None: return ''
            order(node.left)
            self.result += node.data
            order(node.right)
        order(node)
        return self.result

    def porstorder(self, node=None):
        if node is None: node = self.root
        self.result = ''

        def order(node):
            if node is None: return ''
            order(node.left)
            order(node.right)
            self.result += node.data
        order(node)
        return self.result



n = int(input())
connect = {}
for _ in range(n):
    root, left, right = input().split()
    connect[root] = left, right


root = 'A'
tree = Tree(root)
tree.make_tree()

print(tree.preorder())
print(tree.inorder())
print(tree.porstorder())