# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(node, p, q):
            if not node:
                return None

            if (p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val):
                return node
            
            if p.val == node.val:
                return p
            
            if q.val == node.val:
                return q

            
            elif p.val < node.val and q.val < node.val:
                return lca(node.left, p, q)
            
            else:
                return lca(node.right, p, q)
            
        return lca(root, p, q)