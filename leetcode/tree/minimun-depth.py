class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def minDepth(self, root):
        if not root:
            return 0
        stack = [([root], 1)]
        while stack:
            current_level, d = stack.pop()
            next_level = []
            for node in current_level:
                if not node.left and not node.right:
                    return d
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                stack.append((next_level, d + 1))


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
    r = s.minDepth(n0)
    print(r)
