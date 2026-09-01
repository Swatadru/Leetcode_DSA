class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            new_matrix = []
            for i in range(len(mat)):
                new = []
                for j in range(len(mat[i])):
                    new.append(mat[j][i])
                new_matrix.append(new[::-1])
            mat = new_matrix
        return False
