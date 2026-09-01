class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i + 1,len(nums)):
                max_sum = nums[i] + nums[j]
                if max_sum == target:
                    return [i,j]