from typing import List


class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        n = len(prices)
        total_profit = 0

        # Traverse through the array and accumulate profit whenever there's a price increase
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)
