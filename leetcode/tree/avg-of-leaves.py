class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def avgOfLeaves(self, root):
        if root:
            print(root.val)
            self.avgOfLeaves(root.left)
            self.avgOfLeaves(root.right)

if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n1.left = n2
    n1.right = n3
    n4 = TreeNode(15)
    n5 = TreeNode(7)
    n3.left = n4
    n3.right = n5
    s = Solution()
    print(s.avgOfLeaves(n1))

