class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def averageOfLevels(self, root):
        if root is None:
           return []

        result, current = [], [root]
        while current:
           vals, next_level = [], []
           for node in current:
               vals.append(node.val)
               if node.left is not None:
                   next_level.append(node.left)
               if node.right is not None:
                   next_level.append(node.right)
           current = next_level
           result.append(sum(vals)/len(vals))
        return result



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
    print(s.averageOfLevels(n1))
