class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        n = len(s1)
        if s1 == s2:
            return 0
        add = 0
        pairs = 0
        leftover = 0
        i=0
        while i < n:
            if s1[i] == '1' and s2[i] == '0':
                j = i
                while j<n and s1[j] == '1' and s2[j] == '0':
                    j += 1
                run_len = j - i
                pairs += run_len // 2
                leftover += run_len % 2
                i = j
            else:
                if s1[i] == '0' and s2[i] == '1':
                    add += 1
                i += 1
        if leftover > 0 and n == 1:
            return -1
        return add + pairs + 2 * leftover