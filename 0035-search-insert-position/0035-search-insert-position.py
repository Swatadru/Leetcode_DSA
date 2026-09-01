class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)