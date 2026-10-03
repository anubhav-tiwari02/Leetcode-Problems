import heapq
import math
class Solution(object):
    def kClosest(self, points, k):
        heap=[]
        for a,b in points:
            e_dist=math.sqrt(a*a+b*b)
            heapq.heappush(heap,(e_dist,[a,b]))
        ans=[]
        for _ in range(k):
            _,points=heapq.heappop(heap)
            ans.append(points)
        return ans

        