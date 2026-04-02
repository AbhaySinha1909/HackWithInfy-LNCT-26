class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        s = len(nums1)
        p = s//2
        if s % 2 == 0:
            median = (nums1[p-1] + nums1[p]) / 2
        else:
            median = nums1[p]
        return median