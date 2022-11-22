class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        sums = [0] * (n)
        sums[0], sums[1] = cost[0], cost[1]
        for i in range(2, n):
            sums[i] = cost[i] + min(sums[i - 1], sums[i - 2])
        return sums[n - 1]