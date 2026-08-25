class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        factors=[]
        max_elem=max(nums)
        for i in range(1,max_elem+k*2):
            factors.append(i*k)
        for num in factors:
            if num not in nums:
                return num
            else:
                num+=1
        
        