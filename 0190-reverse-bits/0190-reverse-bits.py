class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n,'032b')[::-1]
        return int(binary,2)