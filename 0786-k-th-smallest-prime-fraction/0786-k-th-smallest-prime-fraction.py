import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap=[]
        n=len(arr)
        for i in range(n-1):
            heapq.heappush(min_heap,(arr[i]/arr[n-1],i,n-1))
        for _ in range(k-1):
            val,i,j=heapq.heappop(min_heap)
            if j-1>i:
                heapq.heappush(min_heap,(arr[i]/arr[j-1],i,j-1))
        val,i,j=heapq.heappop(min_heap)
        return [arr[i],arr[j]]

        