class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(path):
            if len(path)==len(nums):
                result.append(path[:])
                return 
            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return result