class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
    
        # Build from row 1 to numRows-1
        for i in range(1, numRows):
            # Start every row with [1]
            row = [1]
            
            # Fill the middle elements
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j]) # 1 + 0 = 1
            
            # End every row with [1]
            row.append(1)
            
            # Add the row to the triangle
            triangle.append(row)
        
        return triangle