class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n =  len(nums)
        x=0
        for i in range(0,n):
            if len(str(nums[i]))  % 2 == 0:
                x+= 1
        return x

