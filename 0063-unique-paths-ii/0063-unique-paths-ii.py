class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp={}
        def solve(i,j):
            if i<0 or j<0:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=solve(i-1,j)+solve(i,j-1)
            return dp[(i,j)]
        return solve(m-1,n-1)
        