class Solution(object):
    def uniquePaths(self, m, n):
        dp={}
        def solve(i,j):
            if i==1 or j==1:
                return 1
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=solve(i-1,j)+solve(i,j-1)
            return dp[(i,j)]
        return solve(m,n)