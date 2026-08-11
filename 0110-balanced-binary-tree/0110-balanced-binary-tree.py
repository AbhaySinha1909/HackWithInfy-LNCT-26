# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(node):
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)
            return (1+max(left, right))

        flagged = True

        stk = [root]        
        while stk:
            Node = stk.pop()
            if abs(depth(Node.left) - depth(Node.right)) > 1:
                flagged = False
            if Node.right: stk.append(Node.right)
            if Node.left: stk.append(Node.left)
        
        return flagged