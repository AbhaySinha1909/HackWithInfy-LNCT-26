# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        m = deque()
        n = deque()
        m.append(p)
        n.append(q)

        while m and n:
            n1 = m.popleft()
            n2 = n.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False

            if n1.val != n2.val:
                return False
            m.append(n1.left)
            m.append(n1.right)
            n.append(n2.left)
            n.append(n2.right)
        
        return not m and not n