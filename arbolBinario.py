class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.value)
            res = res + self.inorder_traversal(root.right)
        return res

    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.value)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.value)
        return res

# Ejemplo de uso
bt = BinaryTree()
keys = [10, 6, 15, 3, 8, 12, 18]

for key in keys:
    bt.insert(key)

print("Inorden:", bt.inorder_traversal(bt.root))
print("Preorden:", bt.preorder_traversal(bt.root))
print("Postorden:", bt.postorder_traversal(bt.root))
