# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stk = [root]

        sum_left_leaf = 0
        while stk:
            node = stk.pop()
            if node.left and not node.left.left and not node.left.right:
                sum_left_leaf += node.left.val
            
            if node.left:
                stk.append(node.left)
            
            if node.right:
                stk.append(node.right)
            
        return sum_left_leaf


