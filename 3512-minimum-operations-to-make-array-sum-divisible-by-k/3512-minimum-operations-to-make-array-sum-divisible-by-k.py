class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        suiiii = sum(nums)
        ans = suiiii % k
        return ans