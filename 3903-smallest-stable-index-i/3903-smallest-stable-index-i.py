class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        left, right = 0 , 0
        while right < len(nums):
            left_elements = nums[left:right+1]
            right_elements = nums[right:]
            maxi = max(left_elements)
            mini = min(right_elements)
            Instability_Score = maxi - mini
            if Instability_Score <= k:
                return right
            right += 1
        return -1