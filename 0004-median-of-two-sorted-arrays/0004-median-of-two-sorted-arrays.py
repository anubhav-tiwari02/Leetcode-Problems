class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        mid_element=n//2
        if n % 2 == 0:
            return (nums1[mid_element - 1]+nums1[mid_element])/2.0
        else:
            return nums1[mid_element]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        