# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root.left and not root.right:
            return [root.val]
        
        stk = [root]
        freq_map = {}
        while stk:
            node = stk.pop()
            if node.val not in freq_map:
                freq_map[node.val] = 1
            else:
                freq_map[node.val] += 1
            
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        
        max_freq = max(freq_map.values())
        result = [val for val, count in freq_map.items() if count == max_freq]
        return result