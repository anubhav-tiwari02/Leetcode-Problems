import heapq
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        speedSum=0
        engineers=list(zip(efficiency,speed))
        engineers.sort(reverse=True)
        speed_heap=[]
        speedSum=0
        ans=0
        for eff,speed in engineers:
            heapq.heappush(speed_heap,speed)
            speedSum+=speed
            if len(speed_heap)>k:
                speedSum-=heapq.heappop(speed_heap)
            ans=max(ans,eff*speedSum)
        return ans %1000000007



        