class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = n//20
        arr.sort()
        nums = arr[k:n-k]
        annn = sum(nums)
        p = len(nums)
        return annn/p