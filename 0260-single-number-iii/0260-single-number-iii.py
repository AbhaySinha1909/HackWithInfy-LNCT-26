class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        result = [num for num, count in counts.items() if count == 1]
        return result