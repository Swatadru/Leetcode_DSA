class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0:
                    dp[row][col] = matrix[row][col]
                else:
                    cost_top = dp[row-1][col]
                    cost_left = dp[row-1][col-1] if col > 0 else float("inf")
                    cost_right = dp[row-1][col+1] if col < n-1 else float("inf")

                    dp[row][col] = matrix[row][col] + min(cost_top, cost_left, cost_right)

        return min(dp[m-1])