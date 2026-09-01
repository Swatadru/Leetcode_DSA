class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1,-1]
        indices = []
        for index, element in enumerate(nums):
            if element == target:
                indices.append(index)
        if indices == []:
            return [-1,-1]
        return [indices[0], indices[-1]] 