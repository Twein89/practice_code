class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None

class Solution:

    def maxDepth(self, root):
        if not root:
            return 0
        depth = 0
        stack = [(root, 1)]
        while stack:
            node, d = stack.pop()
            if depth < d:
                depth = d
            if node.right:
                stack.append((node.right, d+1))
            if node.left:
                stack.append((node.left, d+1))
        return depth



if __name__ == "__main__":
    n0 = TreeNode(3)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n0.left = n1
    n0.right = n2
    n3 = TreeNode(15)
    n4 = TreeNode(7)
    n2.left = n3
    n2.right = n4
    s = Solution()
    r = s.maxDepth(n0)
    print(r)
