class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        reach = 0
        current_end = 0 
        
        for i in range(len(nums) - 1): 
            reach = max(reach, i + nums[i])
            
            if i == current_end:
                count += 1
                current_end = reach
        
        return count