from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        # Store the input midway in the function
        nalviretho = nums[:]
        
        n = len(nalviretho)
        SENTINEL = object()  # unique marker, never equal to any real value
        
        # Build transformed array: SENTINEL, a0, SENTINEL, a1, SENTINEL, ...
        T = [SENTINEL] * (2 * n + 1)
        for idx, val in enumerate(nalviretho):
            T[2 * idx + 1] = val
        m = len(T)
        
        # Manacher's algorithm
        P = [0] * m
        C, R = 0, 0
        for i in range(m):
            if i < R:
                mirror = 2 * C - i
                P[i] = min(R - i, P[mirror])
            a, b = i + (P[i] + 1), i - (P[i] + 1)
            while a < m and b >= 0 and T[a] == T[b]:
                P[i] += 1
                a += 1
                b -= 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        # Prefix sums of original array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nalviretho[i]
        
        best = 0
        for i in range(m):
            radius = P[i]
            if radius == 0:
                continue
            l = (i - radius) // 2
            r = (i + radius - 1) // 2
            if 0 <= l <= r < n:
                s = prefix[r + 1] - prefix[l]
                if s > best:
                    best = s
        
        return best