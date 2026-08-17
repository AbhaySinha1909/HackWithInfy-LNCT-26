# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        result = []
        
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        min_diff = float('inf')
        
        for i in range(1, len(result)):
            min_diff = min(min_diff, abs(result[i] - result[i-1]))
        return min_diff