class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        height=len(matrix)
        width=len(matrix[0])
        maxsize=0

        dp=[[0 for j in range(width+1)] for i in range(height+1)]

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '1':
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j],dp[i][j])+1
                    matrix=max(maxsize,int(dp[i+1][j+1]))
        return maxsize*maxsize