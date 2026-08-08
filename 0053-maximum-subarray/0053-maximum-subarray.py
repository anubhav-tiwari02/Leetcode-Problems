class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum=[0]*len(nums)
        for i in range(len(nums)):
            prefix_sum[i]=max(prefix_sum[i-1]+nums[i],nums[i])
        return max(prefix_sum)