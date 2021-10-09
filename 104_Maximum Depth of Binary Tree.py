# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
        if root is None:
            return 0
        i = maxDepth(root.left)
        j = maxDepth(root.right)
        if i<j: 
            return j+1
        else: 
            return i+1

r1 = TreeNode(3)
a1 = TreeNode(9)
a2 = TreeNode(20)
a3 = TreeNode(15)
a4 = TreeNode(7)

r1.left = a1
r1.right = a2
a2.left = a3
a2.right = a4

x = maxDepth(r1)
print(x)