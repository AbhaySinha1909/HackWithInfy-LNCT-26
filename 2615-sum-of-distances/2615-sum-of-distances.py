class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        for i in range(n):
            sum_ind = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    sum_ind += abs(i - j)
                    j += 1
            arr.append(sum_ind)
            i += 1
        return arr