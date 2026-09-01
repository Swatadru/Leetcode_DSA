class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0

        while True:
            sorted_ok = True
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    sorted_ok = False
                    break

            if sorted_ok:
                return operations

            min_sum = nums[0] + nums[1]
            index = 0

            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    index = i

            nums = nums[:index] + [min_sum] + nums[index + 2:]
            operations += 1