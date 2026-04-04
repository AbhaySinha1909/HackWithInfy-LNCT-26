class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools 
        return [list(p) for p in itertools.permutations(nums)]