class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Travelsal(object):
    def __init__(self):
        self.traverse_path = list()

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)

if __name__ == "__main__":
    a = TreeNode('A')
    b = TreeNode('B')
    c = TreeNode('C')
    a.left = b
    a.right = c
    d = TreeNode('D')
    e = TreeNode('E')
    b.left = d
    b.right = e
    f = TreeNode('F')
    c.left = f
    t = Travelsal()
    t.preorder(a)
    print(t.traverse_path)
    #t.inorder(a)
    #print(t.traverse_path)
    #t.postorder(a)
    #print(t.traverse_path)

