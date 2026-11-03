class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_elem=max(nums)
        moves=0
        for i in range(len(nums)):
            moves+=max_elem-nums[i]
        return moves
        