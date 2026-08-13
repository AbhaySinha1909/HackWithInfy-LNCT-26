# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        l = deque()
        r = deque()

        l.append(root.left)
        r.append(root.right)
        
        while l and r:
        
            node_l = l.popleft()
            node_r = r.popleft()

            if not node_l and not node_r:
                continue

            if not node_l or not node_r:
                return False

            if node_l.val != node_r.val:
                return False

            l.append(node_l.left)
            r.append(node_r.right)
            
            l.append(node_l.right)
            r.append(node_r.left)
            
        
        return True 