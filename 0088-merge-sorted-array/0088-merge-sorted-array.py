class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a1=nums1[:m]
        a2=nums2[:n]
        res=[]
        i=0
        j=0
        while i<len(a1) and j<len(a2) :
            if a1[i]<=a2[j]:
                res.append(a1[i])
                i+=1
            else:
                res.append(a2[j])
                j+=1
        while i<len(a1):
            res.append(a1[i])
            i+=1
        while j<len(a2):
            res.append(a2[j])
            j+=1
        nums1[:]=res
        
            
        