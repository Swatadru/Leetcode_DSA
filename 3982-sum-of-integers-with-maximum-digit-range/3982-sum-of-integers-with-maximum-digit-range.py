class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def digit_range(n):
            digits = [int(d) for d in str(n)]
            return max(digits) - min(digits)
        
        ranges = [digit_range(n) for n in nums]
        max_range = max(ranges)
        return sum(n for n, r in zip(nums, ranges) if r == max_range)