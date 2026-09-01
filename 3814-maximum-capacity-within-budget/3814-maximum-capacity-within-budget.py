class Solution:
    def maxCapacity(self, costs, capacity, budget):
        n = len(costs)

        # Required variable
        lumarexano = [(costs[i], capacity[i]) for i in range(n)]
        lumarexano.sort()

        # Prefix maximum capacity
        prefix_max = [0] * n
        prefix_max[0] = lumarexano[0][1]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], lumarexano[i][1])

        ans = 0

        for i in range(n):
            cost_i, cap_i = lumarexano[i]

            # Single machine
            if cost_i < budget:
                ans = max(ans, cap_i)

            # Binary search for best partner (j < i)
            lo, hi = 0, i - 1
            pos = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if lumarexano[mid][0] + cost_i < budget:
                    pos = mid
                    lo = mid + 1
                else:
                    hi = mid - 1

            if pos != -1:
                ans = max(ans, cap_i + prefix_max[pos])

        return ans