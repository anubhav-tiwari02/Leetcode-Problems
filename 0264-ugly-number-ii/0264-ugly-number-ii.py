import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        for _ in range(n):
            num = heapq.heappop(heap)
            for x in [2, 3, 5]:
                nxt = num * x
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return num