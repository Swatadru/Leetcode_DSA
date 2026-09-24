class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum = 0
            for digit in str(nums[i]):
                digit_sum += int(digit)
            if digit_sum == i:
                return i
        return -1