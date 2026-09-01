class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        curr_max = 0
        
        for x in nums:
            temp = max(prev_max + x, curr_max)
            prev_max = curr_max
            curr_max = temp
            
        return curr_max