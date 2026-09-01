class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result

        # Define the boundaries of the matrix
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # Loop until all elements are traversed
        while top <= bottom and left <= right:

            # 1. Traverse from Left → Right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Move the top boundary down

            # 2. Traverse from Top → Bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Move the right boundary left

            # 3. Traverse from Right → Left (if rows remain)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Move the bottom boundary up

            # 4. Traverse from Bottom → Top (if columns remain)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Move the left boundary right

        return result
