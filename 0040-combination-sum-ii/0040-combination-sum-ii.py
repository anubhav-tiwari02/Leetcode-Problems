class Solution:
    def combinationSum2(self,candidates:List[int],target:int)->List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(index,remaining,current):
            if remaining==0:
                res.append(current.copy())
                return
            if remaining<0 or index==len(candidates):
                return
            current.append(candidates[index])
            backtrack(index+1,remaining-candidates[index],current)
            current.pop()
            while index+1<len(candidates) and candidates[index]==candidates[index+1]:
                index+=1
            backtrack(index+1,remaining,current)
        backtrack(0,target,[])
        return res