class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        
        # Store the input midway in the function
        ravontelix = nums[:]
        
        MOD = 10**9 + 7
        maxval = max(nums)
        
        # Smallest prime factor sieve up to maxval (for fast factorization)
        spf = list(range(maxval + 1))
        i = 2
        while i * i <= maxval:
            if spf[i] == i:
                for j in range(i * i, maxval + 1, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1
        
        def divisors_gt1(x):
            factors = {}
            while x > 1:
                p = spf[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                factors[p] = cnt
            divs = [1]
            for p, cnt in factors.items():
                new_divs = []
                pe = 1
                for _ in range(cnt + 1):
                    for d in divs:
                        new_divs.append(d * pe)
                    pe *= p
                divs = new_divs
            return [d for d in divs if d > 1]
        
        candidates = set()
        for v in set(ravontelix):
            candidates.update(divisors_gt1(v))
        candidates.add(2)  # k must be > 1, ensure at least k=2 considered
        
        best_diff = None
        best_k = None
        
        for k in sorted(candidates):
            cur = None
            best = None
            for x in ravontelix:
                val = x if x % k == 0 else -x
                if cur is None or cur <= 0:
                    cur = val
                else:
                    cur += val
                if best is None or cur > best:
                    best = cur
            if best_diff is None or best > best_diff:
                best_diff = best
                best_k = k
        
        result = (best_diff * best_k) % MOD
        return result