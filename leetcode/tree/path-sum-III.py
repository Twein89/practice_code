from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def pathSum(self, root, sum):
        if root is None:
            return 0
        s = [(root, {root.val: 1})]
        n = 0
        while s:
            node, val_dict = s.pop()
            if sum in val_dict:
                n += val_dict[sum]
            if node.right:
                rdict = {}
                for k in val_dict:
                    rdict[k + node.right.val] = val_dict.get(k, 0)
                rdict[node.right.val] = rdict.get(node.right.val, 0) + 1
                s.append((node.right, rdict))
            if node.left:
                ldict = {}
                for k in val_dict:
                    ldict[k + node.left.val] = val_dict.get(k, 0)
                ldict[node.left.val] = ldict.get(node.left.val, 0) + 1
                s.append((node.left, ldict))
        return n



if __name__ == '__main__':
    n0 = TreeNode(10)
    n1 = TreeNode(5)
    n2 = TreeNode(-3)
    n0.left = n1
    n0.right = n2
    n3 = TreeNode(3)
    n4 = TreeNode(2)
    n5 = TreeNode(11)
    n1.left = n3
    n1.right = n4
    n2.right = n5
    n6 = TreeNode(3)
    n7 = TreeNode(-2)
    n8 = TreeNode(1)
    n3.left = n6
    n3.right = n7
    n4.right = n8
    s = Solution()
    #print(s.hasPathSum(n0, 18))
    print(s.pathSum(n0, 8))

