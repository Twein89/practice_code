class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        elif root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        #if not root:
        #    return 0
        #elif not root.left and not root.right:
        #    return self.sumOfLeftLeaves(root.left)
        #elif not root.left.left and root.left.right:
        #    return root.left.val
        #return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        #if not root:
        #    return 0
        #elif root.left or root.right:
        #    print(root.val)
        #    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        #elif not root.left and not root.left:
        #    return root.left.val

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
    print(s.sumOfLeftLeaves(n1))
