class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        n = len(num)

        if n % 2 == 1:
            return num[n // 2]
        else:
            return (num[n // 2 - 1] + num[n // 2]) / 2