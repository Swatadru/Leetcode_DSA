class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        MOD = 10**9 + 7
        n1, n2, m = len(word1), len(word2), len(target)
        g = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        g[0][0] = 1
        for k in range(m):
            c = target[k]
            new_g = [[0] * (n2 +1) for _ in range(n1 + 1)]
            for j in range(n2 +1):
                pref = 0
                prefix = [0] * (n1+1)
                for i in range(n1 + 1):
                    pref = (pref + g[i][j]) % MOD
                    prefix[i] = pref
                for p in range(n1):
                    if word1[p] == c:
                        new_g[p+1][j] = (new_g[p+1][j] + prefix[p]) % MOD
            for i in range(n1 + 1):
                pref = 0
                prefix = [0] * (n2+1)
                for j in range(n2 + 1):
                    pref = (pref + g[i][j]) % MOD
                    prefix[j] = pref
                for p in range(n2):
                    if word2[p] == c:
                        new_g[i][p+1] = (new_g[i][p+1] + prefix[p]) % MOD
            g = new_g
        total = sum(g[i][j] for i in range(n1 +1) for j in range(n2 +1 ) )% MOD
        def count_subseq(s , t):
            ls , lt = len(s), len(t)
            dpc = [[0] * (lt + 1) for _ in range(ls + 1)]
            for i in range(ls + 1):
                dpc[i][0] = 1
            for i in range(1, ls + 1):
                for j in range(1, lt + 1):
                    dpc[i][j] = dpc[i-1][j]
                    if s[i - 1] == t[j - 1]:
                        dpc[i][j] = (dpc[i][j] + dpc[i-1][j-1]) % MOD
            return dpc[ls][lt]
        only1 = count_subseq(word1, target)
        only2 = count_subseq(word2, target)
        return (total - only1 - only2) % MOD