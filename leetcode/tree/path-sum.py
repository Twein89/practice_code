class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        stack = [(root, sum)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right and node.val == val:
                return True
            if node.right is not None:
                stack.append((node.right, val - node.val))
            if node.left is not None:
                stack.append((node.left, val - node.val))
        return False


if __name__ == '__main__':
    n0 = TreeNode(5)
    n1 = TreeNode(4)
    n2 = TreeNode(8)
    n0.left = n1
    n0.right = n2
    n3 = TreeNode(11)
    n4 = TreeNode(13)
    n5 = TreeNode(4)
    n1.left = n3
    n2.left = n4
    n2.right = n5
    n6 = TreeNode(7)
    n7 = TreeNode(2)
    n8 = TreeNode(1)
    n3.left = n6
    n3.right = n7
    n5.right = n8
    s = Solution()
    print(s.hasPathSum(n0, 23))
