class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        result = []
        def helper(node, result):
            result += str(node.val)

            if not node.left and node.right:
                result.append("()")
            if node.left:
                result.append("(")
                helper(node.left, result)
                result.append(")")
            if node.right:
                result.append("(")
                helper(node.right, result)
                result.append(")")
        helper(t, result)
        return ''.join(result)
