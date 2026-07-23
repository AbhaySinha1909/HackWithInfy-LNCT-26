class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(2 ** n):
            subset = [nums[j] for j in range(n) if (i & (1 << j))]
            result.append(subset)
        return result