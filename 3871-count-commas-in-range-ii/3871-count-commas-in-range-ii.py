class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        factor = 1000
        while n >= factor:
            count += n - factor + 1
            factor *= 1000
        return count