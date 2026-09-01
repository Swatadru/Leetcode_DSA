class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = format(n,'b')
        result = binary.count("1")
        return result