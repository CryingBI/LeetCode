# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric( root: TreeNode) -> bool:
        return isMirror(root,root)
    
    
def isMirror(t1: TreeNode,t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and isMirror(t1.right,t2.left) and isMirror(t1.left,t2.right)
            

r = TreeNode(1)
r1 = TreeNode(2)
r2 = TreeNode(2)
r3 = TreeNode(3)
r4 = TreeNode(4)
r5 = TreeNode(4)
r6 = TreeNode(3)

r.left = r1
r.right = r2
r1.left = r3
r1.right = r4
r2.left = r5
r2.right = r6

a = isSymmetric(r)
print(a)