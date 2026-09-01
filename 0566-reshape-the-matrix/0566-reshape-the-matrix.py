class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat
        
        elements = []
        for i in range(m):
            for j in range(n):
                elements.append(mat[i][j])
        
        new_mat = []
        index = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(elements[index])
                index += 1
            new_mat.append(row)
        return new_mat