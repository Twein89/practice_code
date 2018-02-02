class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        stack = [(root, '')]
        while stack:
            node, path = stack.pop()
            if not path:
                path = str(node.val)
            else:
                path = path + '->' + str(node.val)
            if not node.left and not node.right:
                result.append(path)
            if node.right:
                stack.append((node.right, path))
            if node.left:
                stack.append((node.left, path))
        return result