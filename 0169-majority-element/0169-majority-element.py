class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        max_freq = 0
        majority_element = None
        for i in s:
            freq = nums.count(i)
            if freq > max_freq:
                max_freq = freq
                majority_element = i
        return majority_element