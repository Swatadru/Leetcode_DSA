class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        for i in range(len(nums)-1,-1,-1):
            k -= 1
            if k == 0:
                return nums[i]
        return 0