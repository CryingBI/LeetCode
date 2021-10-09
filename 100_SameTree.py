# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: 
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        return isSameTree(p.right, q.right) and isSameTree(p.left,q.left)
            

root1 = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
root1.left = a
root1.right = b


root2 = TreeNode(1)
c = TreeNode(2)
d = TreeNode(3)
root2.left = c
root2.right = d

m = isSameTree(root1,root2)
print(m)