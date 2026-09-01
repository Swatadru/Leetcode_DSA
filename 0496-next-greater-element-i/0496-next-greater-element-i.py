class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for i in nums1:
            index = nums2.index(i)

            ans = -1

            for j in nums2[index+1:]:
                if j > i:
                    ans = j
                    break

            result.append(ans)

        return result