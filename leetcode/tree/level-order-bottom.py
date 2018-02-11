class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []   
        if not root:
            return result
        def helper(cur_level, result):
            if not cur_level:
                return None
            next_level = []
            temp = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:    
                    next_level.append(node.right)
                temp.append(node.val)    
            #result.insert(0, temp)        
            helper(next_level, result)
            result.append(temp)        
        helper([root], result)
        return result