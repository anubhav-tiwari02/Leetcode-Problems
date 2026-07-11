import heapq
class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        positive=set(positive_feedback)
        negative=set(negative_feedback)
        heap=[]
        for rep,sid in zip(report,student_id):
            score=0
            for word in rep.split():
                if word in positive:
                    score+=3
                elif word in negative:
                    score-=1
            heapq.heappush(heap,(-score,sid))
        ans=[]
        for _ in range(k):
            _,sid=heapq.heappop(heap)
            ans.append(sid)
        return ans

