class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        end_with = {}
        for char in s:
            current_total = sum(end_with.values()) + 1
            end_with[char] = current_total % MOD
        return sum(end_with.values()) % MOD