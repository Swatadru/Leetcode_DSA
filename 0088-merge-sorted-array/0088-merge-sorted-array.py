class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while 0 in nums1[m:]:
            nums1.remove(0)
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        