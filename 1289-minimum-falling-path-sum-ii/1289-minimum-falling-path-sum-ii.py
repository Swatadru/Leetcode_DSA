class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0:
                    dp[row][col] = grid[row][col]
                else:
                    prev_min = float("inf")

                    for k in range(n):
                        if k != col:
                            prev_min = min(prev_min, dp[row-1][k])

                    dp[row][col] = grid[row][col] + prev_min
        return min(dp[m-1])