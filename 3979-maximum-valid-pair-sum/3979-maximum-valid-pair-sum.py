class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        best = nums[0]
        ans = float('-inf')
        for j in range(k, len(nums)):
            best = max(best, nums[j - k])
            ans = max(ans, best + nums[j])
        return ans