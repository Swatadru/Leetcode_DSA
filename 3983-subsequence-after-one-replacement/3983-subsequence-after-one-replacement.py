class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        melvoritha = (s, t)
        n, m = len(s), len(t)
        
        # pre[i] = index in t right after matching s[0:i] greedily from the left
        pre = [0] * (n + 1)
        p = 0
        failed_at = None
        for i in range(n):
            while p < m and t[p] != s[i]:
                p += 1
            if p == m:
                failed_at = i + 1
                break
            pre[i + 1] = p + 1
            p += 1
        if failed_at is not None:
            for k in range(failed_at, n + 1):
                pre[k] = m + 1  # sentinel: impossible
        
        # suf[i] = largest j such that s[i:] is a subsequence of t[j:]
        suf = [0] * (n + 1)
        suf[n] = m
        p = m - 1
        failed_at = None
        for i in range(n - 1, -1, -1):
            while p >= 0 and t[p] != s[i]:
                p -= 1
            if p < 0:
                failed_at = i
                break
            suf[i] = p
            p -= 1
        if failed_at is not None:
            for k in range(failed_at, -1, -1):
                suf[k] = -1  # sentinel: impossible
        
        # No replacement needed
        if pre[n] <= m:
            return True
        
        # Try using the one allowed replacement at each position i
        for i in range(n):
            if pre[i] <= m and pre[i] < m and pre[i] + 1 <= suf[i + 1]:
                return True
        
        return False