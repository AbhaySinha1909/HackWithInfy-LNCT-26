# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def findAverage(node):
            if not node:
                return (0, 0)

            sum_of_node = node.val
            num_of_node = 1

            if node.left:
                left_sum, left_count = findAverage(node.left)
                sum_of_node += left_sum
                num_of_node += left_count
            if node.right:
                right_sum, right_count = findAverage(node.right)
                sum_of_node += right_sum
                num_of_node += right_count 
            return (sum_of_node, num_of_node)
        
        que = deque()
        que.append(root)

        cnt = 0

        while que:
            node = que.popleft()
            summ, numm = findAverage(node)
            avg = summ//numm
            if avg == node.val:
                cnt += 1
            if node.left:que.append(node.left)
            if node.right:que.append(node.right)
        
        return cnt