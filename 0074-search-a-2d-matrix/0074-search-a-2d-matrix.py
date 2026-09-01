class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        find = []
        for i in matrix:
            for j in i:
                if j == target:
                    find.append(j)
        
        if target in find:
            return True
        else:    
            return False