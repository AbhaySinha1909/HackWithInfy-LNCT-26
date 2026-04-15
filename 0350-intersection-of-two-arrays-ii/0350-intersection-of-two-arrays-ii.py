class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_list = []
        for num in nums1:
            if num in nums2:
                my_list.append(num)
        return my_list