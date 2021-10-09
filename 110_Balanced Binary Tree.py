# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#c1:
def isBalanced(root: TreeNode) -> bool:
        if root == None: return True
        if abs(height(root.left)-height(root.right))>1:
            return False
        return isBalanced(root.left) and isBalanced(root.right)
        
        
        
    
def height( node: TreeNode) -> int:
        if node == None: return 0
        return 1 + max(height(node.left),height(node.right))

r = TreeNode(1)
r1 = TreeNode(2)
r2 = TreeNode(2)
r3 = TreeNode(3)
r4 = TreeNode(4)
r5 = TreeNode(4)
r6 = TreeNode(3)

r.left = r1
r.right = r2
r1.right = r3 
r2.right = r5
r5.right = r6
r6.right = r4

print(isBalanced(r))