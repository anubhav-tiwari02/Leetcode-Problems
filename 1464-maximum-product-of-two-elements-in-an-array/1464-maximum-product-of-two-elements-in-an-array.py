class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            return (nums[-1]-1)*(nums[-2]-1)
        