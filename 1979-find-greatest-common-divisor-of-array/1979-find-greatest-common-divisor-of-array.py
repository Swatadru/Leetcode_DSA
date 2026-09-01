class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_value = min(nums)
        max_value = max(nums)
        gcd = float('inf')
        factors_min = []
        factors_max = []        
        for i in range(1,min_value+1):
            if min_value%i == 0:
                factors_min.append(i)
        for j in range(1,max_value+1):
            if max_value%j == 0:
                factors_max.append(j)
        sets_min = set(factors_min)
        sets_max = set(factors_max)
        intersection = sets_max.intersection(sets_min)
        return max(intersection)