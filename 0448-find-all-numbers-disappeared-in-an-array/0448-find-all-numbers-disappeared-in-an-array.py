class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = []
        n = len(nums)
        nums = set(nums)
        for i in range(n):
            if i+1 not in nums:
                s.append(i+1)
        return s